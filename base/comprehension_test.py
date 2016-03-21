if __name__ == "__main__":

    numberList1 = [number for number in range(1,6)]
    print(numberList1)

    numberList2 = [number-1 for number in range(1,6)]
    print(numberList2)

    numberList3 = [number for number in range(1,6) if number % 2 == 1]
    print(numberList3)

    rows = range(1,4)
    cols = range(1,3)
    cells = [(row, col) for row in rows for col in cols]
    for cell in cells:
        print(cell)
