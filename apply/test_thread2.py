import threading
import time
import datetime


def hoge(n, t):
    print(" === start sub thread (method) === ")
    for i in range(n):
        time.sleep(t)
        print("[%s] sub thread (method) : " % threading.currentThread().getName() + str(datetime.datetime.today()))
    print(" === end sub thread (method) === ")


if __name__ == "__main__":
    th = threading.Thread(target=hoge, name="th", args=(5, 5))
    th.start()

    time.sleep(1)

    print(" === start main thread (main) === ")
    for i in range(5):
        time.sleep(10)
        print("main thread : " + str(datetime.datetime.today()))
    print(" === end main thread === ")
