import logging
from src.logging.logger import Logger


class FileLogger(Logger):
    def __init__(self, path, level=None):
        self.level = logging.getLevelName(level) if level else logging.INFO
        self.path = path

    def getLogger(self, name) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(self.level)
        handler = logging.FileHandler(self.path, encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        return logger
