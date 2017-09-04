""" Main application entry point.

    python -m onos_grpc_demo  ...

"""
from __future__ import absolute_import

from argparse import ArgumentParser

from .core import connector
from .core import config
from .core import logger

from .api import device
from .api import application
from .api import link
from .api import group


# Add you command here.
_CMD = {
    "device": device,
    "application": application,
    "link": link,
    "group": group
}


def _dispatch(argv):
    # TODO The following expression has an error but still not know why.
    # cmd, directive, param1 = (list(argv) + [None])[:2]
    argv = argv + [None]
    cmd = argv[0]
    if cmd not in _CMD.keys():
        logger.error("Unsupported command: {}".format(cmd))
        return
    args = {
        "directive": argv[1],
        "params": argv[2:]
    }
    _CMD[cmd](args)


def _parse_args(argv=None):
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", action="append",
            help="config file [etc/config.yml]")
    parser.add_argument("-l", "--level", default="INFO",
            help="logger warning level [INFO]")
    parser.add_argument("-t", "--host", default="localhost",
            help="grpc server host [localhost]")
    parser.add_argument("-p", "--port", default=64000,
            help="grpc server port [64000]")
    args = parser.parse_args(argv)
    if not args.config:
        # Don't specify this as an argument default or else it will always be
        # included in the list.
        args.config = ["etc/config.yml"]
    return args


def _print_welcome():
    """ Welcome message."""
    print("This is a grpc client for onos test.\n"
          "\n"
          "type 'help' for usage message.\n")


def _print_help():
    """ Help message.
    """
    print("usage:\n"
          "  CMD OPTIONS PARAMS\n"
          "CMD:\n"
          "  device|link|group|application\n")


def _parse_cmd(argv=None):
    cmd_str = argv.split(' ')
    if len(cmd_str) >= 2:
        return cmd_str
    else:
        logger.warn("Too few arguments.")
        return None


def main(argv=None):
    """ Execute the application.

    """
    args = _parse_args(argv)
    logger.start(args.level)
    config.load(args.config)
    connector.connect(args.host, args.port)
    # if not connector.is_connected:
    #     logger.warn("Cannot connect to server")
    #     return 0
    logger.info("Connect success.")
    _print_welcome()
    while True:
        cmd = raw_input('onos_grpc_demo > ')
        if cmd == 'exit':
            return 0
        elif cmd == 'help':
            _print_help()
        else:
            args = _parse_cmd(cmd)
            _dispatch(args)

# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
