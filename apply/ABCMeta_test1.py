from abc import *


class Abstract(object, metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def hello(cls):
        print("Abstract hello")


class Implement(Abstract):
    pass


if __name__ == "__main__":

    Abstract.hello()
    Implement.hello()

    # Abstract()
    # TypeError: Can't instantiate abstract class Abstract with abstract methods hello
    # Implement()
    # TypeError: Can't instantiate abstract class Implement with abstract methods hello
