class classX():

    def __init__(self, num):
        self.__num = num

    @property
    def num(self):
        return self.__num 

    @num.setter
    def num(self, num):
        self.__num = num


if __name__ == "__main__":
    cls = classX(12345)
    print(cls.num)

    cls.num = 54321
    print(cls.num)
