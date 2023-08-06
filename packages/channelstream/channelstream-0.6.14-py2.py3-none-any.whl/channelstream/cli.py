from gevent import monkey

monkey.patch_all()

import argparse
import copy
import logging
import pprint
import sys

from six.moves import configparser

import gevent
from gevent.server import StreamServer

import channelstream.wsgi_app as pyramid_app
import channelstream
from channelstream.gc import gc_conns_forever, gc_users_forever
from channelstream.policy_server import client_handle
from channelstream.ws_app import ChatApplicationSocket
from channelstream.utils import set_config_types

from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class RoutingApplication(object):
    def __init__(self, config):
        self.ws_app = WebSocketWSGIApplication(handler_cls=ChatApplicationSocket)
        self.wsgi_app = pyramid_app.make_app(config)

    def __call__(self, environ, start_response):
        if environ["PATH_INFO"] == "/ws":
            environ["ws4py.app"] = self
            return self.ws_app(environ, start_response)

        return self.wsgi_app(environ, start_response)


SHARED_DEFAULTS = {
    "secret": "secret",
    "admin_user": "admin",
    "admin_secret": "admin_secret",
    "cookie_secret": "",
    "gc_conns_after": 30,
    "gc_channels_after": 3600 * 72,
    "wake_connections_after": 5,
    "allow_posting_from": "127.0.0.1",
    "port": 8000,
    "host": "0.0.0.0",
    "debug": False,
    "log_level": "INFO",
    "demo": False,
    "allow_cors": "",
    "validate_requests": True,
    "enforce_https": False,
    "http_scheme": "",
}


def cli_start():
    if sys.version_info.major < 3 or (
        sys.version_info.major <= 3 and sys.version_info.minor < 6
    ):
        logging.warning(
            "\n---\n Branch 0.6.x is the last to support Python older than 3.6\n---\n"
        )

    config = copy.deepcopy(SHARED_DEFAULTS)

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "-i", "--ini", dest="ini", help="Config file path", default=None
    )
    parser.add_argument(
        "-s", "--secret", dest="secret", help="Secret used to secure your API requests"
    )
    parser.add_argument(
        "-u", "--admin_username", dest="admin_user", help="Administrator username"
    )
    parser.add_argument(
        "-a",
        "--admin_secret",
        dest="admin_secret",
        help="Secret used to secure your admin panel",
    )
    parser.add_argument(
        "-host", "--host", dest="host", help="Host ip on which the server listens to"
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        dest="port",
        help="Port on which the server listens to",
    )
    parser.add_argument("-d", "--debug", dest="debug", help="Does nothing for now")
    parser.add_argument(
        "-l", "--log-level", dest="log_level", help="Does nothing for now"
    )
    parser.add_argument("-e", "--demo", dest="demo", help="Does nothing, BW.compat")
    parser.add_argument(
        "-x",
        "--allowed_post_ip",
        dest="allow_posting_from",
        help="comma separated list of ip's " "that can post to server",
    )
    parser.add_argument(
        "-c",
        "--allow_cors",
        dest="allow_cors",
        help="comma separated list of domains's " "that can connect to server",
    )
    parser.add_argument(
        "--validate-requests",
        dest="validate_requests",
        help="Enable timestamp check on signed requests",
    )
    parser.add_argument(
        "--enforce-https", dest="enforce_https", help="Enforce HTTPS connections"
    )
    parser.add_argument(
        "--http-scheme",
        dest="http_scheme",
        help="Sets protocol schema between http/https",
        choices=["http", "https"],
    )
    parser.add_argument(
        "--cookie-secret",
        dest="cookie_secret",
        help="secret for auth_tkt cookie signing. ",
    )
    args = parser.parse_args()

    parameters = (
        "debug",
        "log_level",
        "port",
        "host",
        "secret",
        "admin_user",
        "admin_secret",
        "cookie_secret",
        "allow_posting_from",
        "allow_cors",
        "validate_requests",
        "enforce_https",
        "http_scheme",
    )

    # set values from ini/cli
    if args.ini:
        parser = configparser.ConfigParser()
        parser.read(args.ini)
        settings = dict(parser.items("channelstream"))
        for key in parameters:
            try:
                config[key] = settings[key]
            except KeyError:
                pass
    else:
        for key in parameters:
            conf_value = getattr(args, key)
            if conf_value:
                config[key] = conf_value

    config = set_config_types(config)
    log_level = getattr(logging, (config.get("log_level") or "INFO").upper())
    logging.basicConfig(level=log_level)
    log.setLevel(log_level)
    log.debug(pprint.pformat(config))
    log.info("Starting channelstream {}".format(channelstream.__version__))
    url = "http://{}:{}".format(config["host"], config["port"])

    log.info("Starting flash policy server on port 10843")
    gevent.spawn(gc_conns_forever)
    gevent.spawn(gc_users_forever)
    server = StreamServer(("0.0.0.0", 10843), client_handle)
    server.start()
    log.info("Serving on {}".format(url))
    log.info("Admin interface available on {}/admin".format(url))
    if config["secret"] == "secret":
        log.warning("Using default secret! Remember to set that for production.")
    if config["admin_secret"] == "admin_secret":
        log.warning("Using default admin secret! Remember to set that for production.")

    server = WSGIServer(
        (config["host"], config["port"]),
        RoutingApplication(config),
        log=logging.getLogger("channelstream.WSGIServer"),
    )
    server.serve_forever()
