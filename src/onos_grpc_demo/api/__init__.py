""" Application commands common to all interfaces.

"""
from .device import main as device
from .link import main as link
from .group import main as group
from .application import main as application


__all__ = "device", "link", "group", "application"
