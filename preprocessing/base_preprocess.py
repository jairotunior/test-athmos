from abc import ABC, abstractmethod

class PreProcess(ABC):

    @abstractmethod
    def transform(self):
        pass