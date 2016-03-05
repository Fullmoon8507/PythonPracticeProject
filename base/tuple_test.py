if __name__ == "__main__":
    a_tuple = ("a", "b", "mpilgrim", "z", "example")

    print(a_tuple);
    print(a_tuple[0]);
    print(a_tuple[-1]);
    print(a_tuple[1:3]);
    print(a_tuple.index("example"))
    print("z" in a_tuple)

    #以下の内容はエラーとなるため、コメント化(タプルのため)
    #a_tuple.append("new")
    #a_tuple.remove("z")
