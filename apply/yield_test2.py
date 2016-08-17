def fruits_list():
    yield "apple"
    yield "banana"
    yield "orange"


if __name__ == "__main__":
    gen = fruits_list()
    print(next(gen))  # apple
    print(next(gen))  # banana
    print(next(gen))  # orange
    # print(next(gen))  # StepIteration
    print()

    gen = fruits_list()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print()

    print(next(fruits_list()))
    print(next(fruits_list()))
    print(next(fruits_list()))
    print()

    print(type(fruits_list()))
