if __name__ == "__main__":
    #数値と文字列の混合
    a = [
        10,
        'ABC'
    ]

    for n in a:
        print(n)
    print()

    #listの結合も可能
    b = [1,2,3,]
    c = [4,5,6,]
    d = b + c

    print("-List1-")
    print(b);
    print("-List2-")
    print(c);
    print("-List1 + List2-")
    print(b + c)
    print()

    #List内にListを作成
    e = [[1,2],[3,4],[5,6]]
    print(e)
    for list in e:
        for n in list:
            print(n)
    print()

