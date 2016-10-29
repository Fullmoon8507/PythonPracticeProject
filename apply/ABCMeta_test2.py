from abc import *

class Abstract(object, metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def hello(cls):
        print("Abstract hello")


class Implement(Abstract):
    
    @classmethod
    def say(cls):
        print("Implement class-method say")

    def yeah(self):
        print("Implement instance-method yeah")


if __name__ == "__main__":
    Implement()
    # TypeError: Can't instantiate abstract class Implement with abstract methods hello
    # Abstract抽象クラスのhello抽象メソッドを実装しないとエラー
