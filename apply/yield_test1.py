def fruits_list():
    yield "apple"
    yield "banana"
    yield "orange"


if __name__ == "__main__":
    for fruit in fruits_list():
        print(fruit)