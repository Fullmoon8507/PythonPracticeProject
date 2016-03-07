class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        self.count = 1

if __name__ == "__main__":
    a1 = MyClass()
    a2 = MyClass()

    print("a1.count:", a1.count)
    print("a2.count:", a2.count)
    print("MyClass.count:", MyClass.count)
