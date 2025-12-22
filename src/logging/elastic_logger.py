from datetime import datetime
from src.logging.logger import Logger
import logging
from elasticsearch import Elasticsearch


class EsHandler(logging.Handler):
    def __init__(self, host: str, index: str):
        super().__init__()
        self.es = Elasticsearch(hosts=[host])
        self.index = index

    def emit(self, record: logging.LogRecord):
        try:
            self.es.index(index=self.index,
                          document={'message': record.getMessage(), 'time': datetime.now(), 'logger': record.name,
                                    'level': record.levelname})
        except Exception as e:
            print(e)

class EsLogger(Logger):

    def __init__(self, host: str, index: str, level=None):
        self.level = logging.getLevelName(level) if level else logging.INFO
        self.host = host
        self.index = index

    def getLogger(self, name) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(self.level)
        logger.addHandler(EsHandler(self.host, self.index))
        return logger
