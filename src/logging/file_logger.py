import logging
from src.logging.logger import Logger


class FileLogger(Logger):
    def __init__(self, path, level=None):
        level = logging.getLevelName(level) if level else logging.INFO
        logging.basicConfig(filename=path, encoding='utf-8', level=level)

    def getLogger(self, name) -> logging.Logger:
        return logging.getLogger()



