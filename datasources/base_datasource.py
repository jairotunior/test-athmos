from abc import ABC, abstractmethod

class BaseDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _save(self):
        pass