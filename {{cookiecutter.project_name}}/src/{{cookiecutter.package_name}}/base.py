"""{{cookiecutter.package_name}}.base.

This Base class inherits from our LoggingBase metaclass and gives us
shared logging across any class inheriting from Base.
"""
from .utils.logger import LoggingBase


class Base(metaclass=LoggingBase):
    """Base class to all other classes within this project."""
    pass
