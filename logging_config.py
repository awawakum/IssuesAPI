import logging
from logging.config import dictConfig
from config import settings
import os


def setup_logging() -> None:
    """Configure logging for the application using settings.

    Supports console logging always and optional file logging with rotation.
    """
    level = settings.LOG_LEVEL.upper() if hasattr(settings, "LOG_LEVEL") else "INFO"

    formatter = {
        "()": "logging.Formatter",
        "fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "datefmt": "%Y-%m-%d %H:%M:%S",
    }

    handlers = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": level,
        }
    }

    # Optionally add file handler
    if getattr(settings, "LOG_TO_FILE", False):
        log_path = getattr(settings, "LOG_FILE_PATH", "logs/issuesapi.log")
        # Ensure directory exists
        log_dir = os.path.dirname(log_path) or "logs"
        try:
            os.makedirs(log_dir, exist_ok=True)
        except Exception:
            # best-effort: if we can't create directory, fallback to console only
            pass

        if getattr(settings, "LOG_ROTATE", True):
            handlers["file"] = {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "level": level,
                "filename": log_path,
                "maxBytes": getattr(settings, "LOG_MAX_BYTES", 10 * 1024 * 1024),
                "backupCount": getattr(settings, "LOG_BACKUP_COUNT", 5),
                "encoding": "utf-8",
            }
        else:
            handlers["file"] = {
                "class": "logging.FileHandler",
                "formatter": "default",
                "level": level,
                "filename": log_path,
                "encoding": "utf-8",
            }

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"default": formatter},
        "handlers": handlers,
        "loggers": {
            "uvicorn": {"handlers": list(handlers.keys()), "level": level, "propagate": False},
            "uvicorn.error": {"handlers": list(handlers.keys()), "level": level, "propagate": False},
            "uvicorn.access": {"handlers": [k for k in handlers.keys() if k == "console"], "level": "INFO", "propagate": False},
            "sqlalchemy.engine": {
                "handlers": list(handlers.keys()),
                "level": "INFO" if getattr(settings, "DATABASE_ECHO", False) else "WARNING",
                "propagate": False,
            },
        },
        "root": {"handlers": list(handlers.keys()), "level": level},
    }

    dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
