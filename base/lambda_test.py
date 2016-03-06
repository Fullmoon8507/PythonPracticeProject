class Album(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

if __name__ == "__main__":

    #基本的なラムダの使い方
    myfunc = lambda x: x ** 2
    print(myfunc(5))
    print(myfunc(6))
    print()

    #sorted()との使い方
    l1 = [(7,2), (3,4), (5,5), (10,3)]
    l2 = sorted(l1, key=lambda x: x[1])
    print("ソート前")
    print(l1)
    print("ソート後")
    print(l2)
    print()

    #map()との使い方
    l3 = [1,3,5]
    l4 = map(lambda x: x ** 2, l3)
    print("[2乗前]")
    for a in l3:
        print(a, end=" ")
    print()
    print("[2乗後]")
    for a in l4:
        print(a, end=" ")
    print()
    print()

    #filter()との使い方
    a1 = Album("A Hard Day's Night", 'The Beatles')
    a2 = Album("The Rolling Stones", 'The Rolling Stones')
    a3 = Album("Abbey Road", 'The Beatles')
    albums = [a1, a2, a3]
    albums_beatles = filter(lambda album: album.artist == 'The Beatles', albums)
    print("[フィルター前]")
    for a in albums:
        print(a.artist, "-", a.title)
    print("[フィルター後]")
    for a in albums_beatles:
        print(a.artist, "-", a.title)
    print()
