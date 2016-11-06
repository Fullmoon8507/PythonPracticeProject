from abc import ABCMeta, abstractmethod


class AbstractItem(metaclass=ABCMeta):

    def __init__():
        pass

    @abstractmethod
    def composite(self):
        pass

    def __iter__(self):
        return iter([])
