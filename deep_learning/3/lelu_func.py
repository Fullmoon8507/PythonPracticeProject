import numpy as np
import matplotlib.pylab as plt

def lelu_functin(x):
    return np.maximum(0, x)

if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y = lelu_functin(x)

    plt.plot(x,y)
    plt.ylim(-0.5, 5.5) # y軸の範囲を指定
    plt.show()
