""" Implement the link command.

"""
from __future__ import absolute_import

from ..core import logger


def main(**kwargs):
    """ Execute the command.
    
    """
    # Using kwargs to provide a generic interface across all commands.
    logger.debug("executing link command")
    return 0
