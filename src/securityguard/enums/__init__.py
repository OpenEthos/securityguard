"""Enums used throughout the SecurityGuard application."""

from enum import Enum

class Type(Enum):
    """Enumeration of different types used in SecurityGuard."""
    CONFIG = "config"
    MANIFEST = "manifest"
    REPORT = "report"
    HOST = "host"

class Status(Enum):
    """Enumeration of status types used in SecurityGuard."""
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"
    INFO = "info"
    ERROR = "error"
