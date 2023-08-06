"""Traefik implementation

Custom proxy implementations can subclass :class:`Proxy`
and register in JupyterHub config:

.. sourcecode:: python

    from mymodule import MyProxy
    c.JupyterHub.proxy_class = MyProxy

Route Specification:

- A routespec is a URL prefix ([host]/path/), e.g.
  'host.tld/path/' for host-based routing or '/path/' for default routing.
- Route paths should be normalized to always start and end with '/'
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import json
from urllib.parse import urlparse
from traitlets import Any, default, Unicode

from aioetcd3.client import client
from aioetcd3 import transaction
from aioetcd3.kv import KV
from aioetcd3.help import range_prefix

from . import traefik_utils
from jupyterhub_traefik_proxy import TraefikProxy


class TraefikEtcdProxy(TraefikProxy):
    """JupyterHub Proxy implementation using traefik and etcd"""

    etcd_client = Any()

    @default("etcd_client")
    def _default_client(self):
        etcd_service = urlparse(self.etcd_url)
        return client(
            endpoint=str(etcd_service.hostname) + ":" + str(etcd_service.port)
        )

    etcd_url = Unicode(
        "http://127.0.0.1:2379", config=True, help="""The URL of the etcd server"""
    )

    etcd_traefik_prefix = Unicode(
        "/traefik/",
        config=True,
        help="""The etcd key prefix for traefik static configuration""",
    )

    etcd_jupyterhub_prefix = Unicode(
        "/jupyterhub/",
        config=True,
        help="""The etcd key prefix for traefik dynamic configuration""",
    )

    async def _setup_traefik_static_config(self):
        await super()._setup_traefik_static_config()
        kv = {}

        def get_etcd_kvs(d, etcd_key):
            for k, v in d.items():
                if isinstance(v, dict):
                    new_key = etcd_key + k + "/"
                    get_etcd_kvs(v, new_key)
                else:
                    kv[etcd_key + k] = v

        get_etcd_kvs(self.static_config, self.etcd_traefik_prefix)

        success = [
            KV.put.txn(
                self.etcd_traefik_prefix + "etcd/endpoint",
                str(urlparse(self.etcd_url).hostname)
                + ":"
                + str(urlparse(self.etcd_url).port),
            ),
            KV.put.txn(
                self.etcd_traefik_prefix + "etcd/prefix", self.etcd_traefik_prefix
            ),
            KV.put.txn(self.etcd_traefik_prefix + "etcd/useapiv3", "true"),
            KV.put.txn(self.etcd_traefik_prefix + "etcd/watch", "true"),
            KV.put.txn(self.etcd_traefik_prefix + "providersThrottleDuration", "1"),
        ]

        for key, value in kv.items():
            if isinstance(value, bool):
                value = str(value).lower()
            if isinstance(value, list):
                for i in range(len(value)):
                    key += "/" + str(i)
                    value = value[i]
            success.append(KV.put.txn(key.lower(), value))

        status, response = await self.etcd_client.txn(
            compare=[], success=success, fail=[]
        )

        if status:
            self.log.error(
                "Couldn't set up traefik's static config. Response: %s", response
            )

    def _start_traefik(self):
        self.log.info("Starting traefik...")
        try:
            self._launch_traefik(config_type="etcd")
        except FileNotFoundError as e:
            self.log.error(
                "Failed to find traefik \n"
                "The proxy can be downloaded from https://github.com/containous/traefik/releases/download."
            )
            raise

    async def start(self):
        """Start the proxy.

        Will be called during startup if should_start is True.

        **Subclasses must define this method**
        if the proxy is to be started by the Hub
        """
        # TODO: investigate deploying a traefik cluster instead of a single instance!
        await super().start()
        await self._wait_for_static_config(provider="etcdv3")

    async def stop(self):
        """Stop the proxy.

        Will be called during teardown if should_start is True.

        **Subclasses must define this method**
        if the proxy is to be started by the Hub
        """
        await super().stop()

    async def add_route(self, routespec, target, data):
        """Add a route to the proxy.

        **Subclasses must define this method**

        Args:
            routespec (str): A URL prefix ([host]/path/) for which this route will be matched,
                e.g. host.name/path/
            target (str): A full URL that will be the target of this route.
            data (dict): A JSONable dict that will be associated with this route, and will
                be returned when retrieving information about this route.

        Will raise an appropriate Exception (FIXME: find what?) if the route could
        not be added.

        The proxy implementation should also have a way to associate the fact that a
        route came from JupyterHub.
        """
        self.log.info("Adding route for %s to %s.", routespec, target)

        routespec = self.validate_routespec(routespec)
        route_keys = traefik_utils.generate_route_keys(self, routespec)

        # Store the data dict passed in by JupyterHub
        data = json.dumps(data)
        rule = traefik_utils.generate_rule(routespec)

        # To be able to delete the route when routespec is provided
        jupyterhub_routespec = self.etcd_jupyterhub_prefix + routespec

        status, response = await self.etcd_client.txn(
            compare=[],
            success=[
                KV.put.txn(jupyterhub_routespec, target),
                KV.put.txn(target, data),
                KV.put.txn(route_keys.backend_url_path, target),
                KV.put.txn(route_keys.backend_weight_path, "1"),
                KV.put.txn(route_keys.frontend_backend_path, route_keys.backend_alias),
                KV.put.txn(route_keys.frontend_rule_path, rule),
            ],
            fail=[],
        )

        if status:
            self.log.info(
                "Added backend %s with the alias %s.", target, route_keys.backend_alias
            )
            self.log.info(
                "Added frontend %s for backend %s with the following routing rule %s.",
                route_keys.frontend_alias,
                route_keys.backend_alias,
                routespec,
            )
        else:
            self.log.error(
                "Couldn't add route for %s. Response: %s", routespec, response
            )

        if self.should_start:
            try:
                # Check if traefik was launched
                pid = self.traefik_process.pid
            except AttributeError:
                self.log.error(
                    "You cannot add routes if the proxy isn't running! Please start the proxy: proxy.start()"
                )
                raise
        await self._wait_for_route(routespec, provider="etcdv3")

    async def delete_route(self, routespec):
        """Delete a route with a given routespec if it exists.

        **Subclasses must define this method**
        """
        routespec = self.validate_routespec(routespec)
        jupyterhub_routespec = self.etcd_jupyterhub_prefix + routespec
        value, _ = await self.etcd_client.get(jupyterhub_routespec)
        if value is None:
            self.log.warning("Route %s doesn't exist. Nothing to delete", routespec)
            return

        target = value.decode()
        route_keys = traefik_utils.generate_route_keys(self, routespec)

        status, response = await self.etcd_client.txn(
            compare=[],
            success=[
                KV.delete.txn(jupyterhub_routespec),
                KV.delete.txn(target),
                KV.delete.txn(route_keys.backend_url_path),
                KV.delete.txn(route_keys.backend_weight_path),
                KV.delete.txn(route_keys.frontend_backend_path),
                KV.delete.txn(route_keys.frontend_rule_path),
            ],
            fail=[],
        )
        if status:
            self.log.info("Routespec %s was deleted.", routespec)
        else:
            self.log.error(
                "Couldn't delete route %s. Response: %s", routespec, response
            )

    async def get_all_routes(self):
        """Fetch and return all the routes associated by JupyterHub from the
        proxy.

        **Subclasses must define this method**

        Should return a dictionary of routes, where the keys are
        routespecs and each value is a dict of the form::

          {
            'routespec': the route specification ([host]/path/)
            'target': the target host URL (proto://host) for this route
            'data': the attached data dict for this route (as specified in add_route)
          }
        """
        all_routes = {}
        routes = await self.etcd_client.range(range_prefix(self.etcd_jupyterhub_prefix))

        for key, value, _ in routes:
            # Strip the "/jupyterhub" prefix from the routespec
            routespec = key.decode().replace(self.etcd_jupyterhub_prefix, "")
            target = value.decode()

            value, _ = await self.etcd_client.get(target)
            if value is None:
                data = None
            else:
                data = value

            all_routes[routespec] = {
                "routespec": routespec,
                "target": target,
                "data": json.loads(data),
            }

        return all_routes

    async def get_route(self, routespec):
        """Return the route info for a given routespec.

        Args:
            routespec (str):
                A URI that was used to add this route,
                e.g. `host.tld/path/`

        Returns:
            result (dict):
                dict with the following keys::

                'routespec': The normalized route specification passed in to add_route
                    ([host]/path/)
                'target': The target host for this route (proto://host)
                'data': The arbitrary data dict that was passed in by JupyterHub when adding this
                        route.

            None: if there are no routes matching the given routespec
        """
        routespec = self.validate_routespec(routespec)
        jupyterhub_routespec = self.etcd_jupyterhub_prefix + routespec

        value, _ = await self.etcd_client.get(jupyterhub_routespec)
        if value == None:
            return None
        target = value.decode()
        value, _ = await self.etcd_client.get(target)
        if value is None:
            data = None
        else:
            data = value

        return {"routespec": routespec, "target": target, "data": json.loads(data)}
