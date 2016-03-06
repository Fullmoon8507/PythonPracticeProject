if __name__ == "__main__":
    a = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print("整数のリスト")
    for n in a:
        print(n)
    print("要素数：" + str(len(a)))
    print("")

    print("２番目の項目：" + str(a[1]));
    print("３番目〜５番目の項目：" + str(a[2:5]))
    print("一番最後の項目：" + str(a[-1]))
    print("後ろから２〜３番目の項目：" + str(a[-4:-2]))
    print("")

