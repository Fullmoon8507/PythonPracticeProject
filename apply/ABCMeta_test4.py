from abc import *

class Abstract(object, metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def hello(cls):
        print("Abstract hello")

    def say(self):
        print("Abstract say")


class Implement(Abstract):
    
    def hello(self):
        print("Implement hello")

    @classmethod
    def say(cls):
        print("Implement say")

if __name__ == "__main__":
    
    impl = Implement()
    impl.hello()
    impl.say()

    # Implement.hello()
    # TypeError: hello() missing 1 required positional argument: 'self'

    Implement.say()
