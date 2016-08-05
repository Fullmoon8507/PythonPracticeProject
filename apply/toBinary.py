'''
Created on 2016/05/25

@author: User
'''

def toBinary(n):
    x = ""
    while n > 0:
        x = str(n%2) + str(x)
        n //= 2

    if n == 1:
        x = "1" + x

    return x

if __name__ == '__main__':
    print("input >>> ", end="")
    inStr = input()
    
    x = toBinary(int(inStr))

    print("１０進数：" + inStr)
    print("２進数：" + x)