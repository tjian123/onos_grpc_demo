""" Implement the device command.

"""
from __future__ import absolute_import

from ..core import logger
from ..core import connector

from ..proto import DeviceServiceNb_pb2
from ..proto import DeviceServiceNb_pb2_grpc


def _parse_arg(stub, argv=None):
    return args


def _get_devices(stub, argv=None):
    logger.info("get all the devices.")
    device_reply = stub.getDevices(DeviceServiceNb_pb2.getDevicesRequest())
    print("getDevices request")
    for device in device_reply.device:
        print("device : %s" % device.device_id)


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
    # TODO It seems difficult to confirm whether the channel is connected.
    # if not connector.is_connected:
    #     logger.warn("Cannot connect with server.")
    #     return 0
    stub = DeviceServiceNb_pb2_grpc.DeviceServiceStub(connector.channel)
    commands[argv['directive']](stub, argv['params'])
    return 0
