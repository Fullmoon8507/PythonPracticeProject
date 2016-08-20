'''
Created on 2016/08/19

@author: User
'''

import time

if __name__ == '__main__':
    # for分のスピードテスト

    # 利用するデータ
    data = [i for i in range(10000000)]

    # 通常のfor文
    list = []
    start = time.clock()
    for d in data:
        if d % 2 == 0:
            list.append(d)
    end = time.clock()
    time1 = end - start

    # リスト内包表記
    start = time.clock()
    list = [d for d in data if d % 2 == 0]
    end = time.clock()
    time2 = end - start

    # filterとラムダ式
    start = time.clock()
    list = filter(lambda d: d % 2 == 0, data)
    end = time.clock()
    time3 = end - start

    print("time1（通常のfor文） = " + str(time1))
    print("time2（リスト内表記)）= " + str(time2))
    print("time3（ラムダとfilter） = " + str(time3))
    print("time2 / time1 = " + str((time2 / time1)))
    print("time3 / time1 = " + str((time3 / time1)))
