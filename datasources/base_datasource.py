from abc import ABC, abstractmethod

class BaseDataSource(ABC):

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, index):
        pass

    @abstractmethod
    def modify(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_list(self):
        pass

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _save(self):
        pass