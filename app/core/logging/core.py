import enum
import logging
import logging.config
import pathlib

import yaml

main_logger = logging.getLogger("__main__")


class LoggingLevels(enum.StrEnum):
    debug = "DEBUG"
    info = "INFO"
    warn = "WARN"
    error = "ERROR"


def configure_logging():
    config_path = pathlib.Path.cwd() / "app" / "core" / "logging" / "config.yml"
    with open(file=config_path, mode="r") as obj:  # noqa: UP015
        logging_config = yaml.safe_load(obj)

    logging_level = "INFO"
    logging_levels = list(LoggingLevels)

    if logging_level not in logging_levels:
        logging_level = LoggingLevels.warn

    if "loggers" in logging_config:
        for logger in logging_config["loggers"].values():
            logger["level"] = logging_level

    if "root" in logging_config:
        logging_config["root"]["level"] = logging_level

    logging.config.dictConfig(logging_config)
