from abc import ABC, abstractmethod


class BaseConnection(ABC):

    @abstractmethod
    def query(self, query):
        pass
