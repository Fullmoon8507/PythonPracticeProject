import numpy as np

if __name__ == "__main__":
    x = np.array([[51, 55], [14, 19], [0, 4]])
    
    print("x = \n" + str(x))
    print()

    print("x[0] = " + str(x[0]))
    print("x[0][1] = " + str(x[0][1]))
    print()

    for row in x:
        print(row)

    y = x.flatten()
    print("y = x.flatten() = " + str(y))
    print(y[np.array([0,2,4])])
    print()

    print("y > 15 : " + str(y>15))
    print(y[y>15])
