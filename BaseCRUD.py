from abc import ABC, abstractmethod


class BaseCrud(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self, conditions=None):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self, conditions=None):
        pass