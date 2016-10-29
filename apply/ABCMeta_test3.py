from abc import *

class Abstract(object, metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def hello(cls):
        print("Abstract hello")


class Implement(Abstract):
    
    def hello(self):
        print("Implement hello")


if __name__ == "__main__":
    
    # 抽象クラスの抽象メソッドがクラスメソッドでも、
    # 実装クラスはインスタンスメソッドで実装可能。
    impl = Implement()
    impl.hello()
