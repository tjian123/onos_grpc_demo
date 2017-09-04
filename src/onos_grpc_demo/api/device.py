""" Implement the device command.

"""
from __future__ import absolute_import

from ..core import logger
from ..core import connector


def _parse_arg(stub, argv=None):
    return args


def _get_devices(stub, argv=None):
    logger.info("get all the devices.")


def _get_device(stub, argv=None):
    logger.info("get device info.")


def main(argv):
    """ Execute the command.
    
    """
    # Using kwargs to provide a generic interface across all commands.
    logger.debug("executing device command")
    commands = {
        "list": _get_devices,
        "info": _get_device,
    }
    if not connector.is_connected:
        logger.warn("Cannot connect with server.")
        return 0
    stub = device_pb2_grpc.DeviceServiceStub(connector.channel)
    commands[argv['directive']](stub, argv['params'])
    return 0
