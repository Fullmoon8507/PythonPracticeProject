###################################################################
# インスタンス変数が存在しない場合、「インスタンス．変数名」は
# クラス変数を参照する。
# 「インスタンス変数．変数名」に値を代入した時点で
# インスタンス変数が生成され、以降はインスタンス変数が参照される。
###################################################################
class MyClass:
    PI = 3.14

if __name__ == "__main__":
    a1 = MyClass()
    a2 = MyClass()

    print(a1.PI)        # クラス変数 MyClass.PI(3.14)が参照される

    a1.PI = 3.141593    # インスタンス変数a1.PIが生成される

    print(a1.PI)        # インスタンス変数a1.PI(3.141593)
    print(a2.PI)        # クラス変数 MyClass.PI(3.14)が参照される
