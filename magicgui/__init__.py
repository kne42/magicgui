"""magicgui is a utility for generating a GUI from a python function"""

__author__ = """Talley Lambert"""
__email__ = "talley.lambert@gmail.com"
__version__ = "0.0.7"

from .core import magicgui, register_type
from . import _qt as api

event_loop = api.event_loop

__all__ = ["magicgui", "register_type", "event_loop", "api"]
