import logging


class FileLogger:
    def __init__(self, file_path):
        # self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename=file_path, encoding='utf-8', level=logging.INFO)

