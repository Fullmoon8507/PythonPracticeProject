import numpy as np

if __name__ == "__main__":
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[3, 0], [0, 6]])

    print("x = \n" + str(x))
    print("y = \n" + str(y))
    print()

    print("x + y = \n" + str(x+y))
    print("x - y = \n" + str(x-y))
    print("x * y = \n" + str(x*y))
    print("x * 10 = \n" + str(x*10))
