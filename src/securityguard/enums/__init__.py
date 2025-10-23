from enum import Enum

class Type(Enum):
    CONFIG = "config"
    MANIFEST = "manifest"
    REPORT = "report"
    HOST = "host"

class Status(Enum):
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"
    INFO = "info"
    ERROR = "error"
    


