from abc import ABC
from typing import Any


class Repo(ABC):

    def insert_one(self, data) -> str:
        pass

    def find_all(self, query: dict[str, Any]):
        pass

    def find_one(self, query: dict[str, Any]):
        pass

    def delete_one(self, query: dict[str, Any]):
        pass

    def exists(self, query: dict[str, Any]):
        pass
