from abc import ABC
import logging


class Logger(ABC):
    def get_logger(self) -> logging.Logger:
        pass
