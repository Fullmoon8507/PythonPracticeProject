if __name__ == "__main__":
    d = {'Yamada':30, 'Suzuki':40, 'Tanaka':80}

    for k, v in d.items():
        print(k,v)
    print()

    for k in d.keys():
        print(k, d[k])
    print()
