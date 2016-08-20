'''
Created on 2016/08/20

@author: User
'''

if __name__ == '__main__':

    # 基本的な使い方
    print((lambda x, y: x + y)(3, 4))

    # 変数にラムダ式を格納し、実行する使い方
    func = lambda x: x**2
    print(func(4))

    # map関数と組み合わせた使い方
    ite = map(func, range(1, 11))
    print(list(ite))

    # map関数とfilter関数の組み合わせた使い方
    ite = map(func, range(1, 11))
    filterFunc = lambda x: x % 2 == 0
    filterIte = filter(filterFunc, ite)
    print(list(filterIte))
