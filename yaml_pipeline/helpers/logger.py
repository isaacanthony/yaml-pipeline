"""Logging wrapper"""
import logging


# Intentionally using name that matches logging.getLogger.
# pylint: disable=invalid-name
def getLogger() -> logging.Logger:
    """Logging wrapper"""
    logging.basicConfig(format="%(asctime)s %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger
