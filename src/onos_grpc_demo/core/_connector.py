""" Global grpc connector.

This module defines a global connector. Other modules should use this connector
to communicate with a special grpc server.
"""
from __future__ import absolute_import

import grpc

from ._logger import logger


__all__ = "connector",


class _Connector(object):
    """ A connector that wrapping the grpc client stub.

    """
    def __init__(self):
        # TODO Current we cannot confirm weather the channel is available before sending a grpc request.
        self.is_connected = False
        self.channel = None

    def connect(self, host, port):
        target = "%s:%s" % (host, port)
        logger.info("Trying to connect server: {:s}.".format(target))
        self.channel = grpc.insecure_channel(target)

connector = _Connector()
