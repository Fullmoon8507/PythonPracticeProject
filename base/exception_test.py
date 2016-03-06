def exception_test(value1, value2):
    print("==== calc start ====")

    result = 0

    try:
        result = value1 + value2
    except:
        print("計算出来ませんでした！")
    finally:
        print("==== calc end ====")

    return result

if __name__ == "__main__":
    print(exception_test(100, 200))
    print(exception_test(100, "200"))
