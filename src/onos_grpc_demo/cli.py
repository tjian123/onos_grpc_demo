""" Implementation of the command line interface.

"""
from __future__ import absolute_import

from argparse import ArgumentParser

from . import __version__
from .api import device
from .api import application
from .api import link
from .api import group
from .core import config
from .core import logger


__all__ = "main"

# Add you command here.
_CMD = {
    "device": device,
    "application": application,
    "link": link,
    "group": group
}


def _cmdline(argv=None):
    """ Parse command line arguments.

    """
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", action="append",
            help="config file [etc/config.yml]")
    parser.add_argument("-v", "--version", action="version",
            version="onos_grpc_demo {:s}".format(__version__),
            help="print version and exit")
    parser.add_argument("-l", "--level", default="INFO",
            help="logger warning level [INFO]")
    parser.add_argument("-t", "--host", default="localhost",
            help="grpc server host [localhost]")
    parser.add_argument("-p", "--port", default="64000",
            help="grpc server port [64000]")
    subparsers = parser.add_subparsers(title="commands")
    for (k, v) in _CMD.iteritems():
        cmd_parser = subparsers.add_parser(k)
        cmd_parser.set_defaults(command=v)
    args = parser.parse_args(argv)
    if not args.config:
        # Don't specify this as an argument default or else it will always be
        # included in the list.
        args.config = ["etc/config.yml"]
    return args


def main(argv=None):
    """ Execute the application CLI.

    Arguments are taken from sys.argv by default.

    """
    args = _cmdline(argv)
    logger.start(args.level)
    logger.info("starting execution")
    config.load(args.config)
    args.command(**vars(args))
    logger.info("successful completion")
    return 0
 

# Make the module executable.

if __name__ == "__main__":
    try:
        status = main()
    except:
        logger.critical("shutting down due to fatal error")
        raise  # print stack trace
    else:
        raise SystemExit(status)
