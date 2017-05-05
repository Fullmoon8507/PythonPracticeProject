import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # 0から6まで0.1刻みで生成
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()
