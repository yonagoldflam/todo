from abc import ABC
import logging


class Logger(ABC):
    def getLogger(self, name) -> logging.Logger:
        pass
