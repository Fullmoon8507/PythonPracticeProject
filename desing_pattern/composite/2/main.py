from item import Item


def main():
    pencil = Item.create("Pencil", 0.40)
    ruler = Item.create("Ruler", 1.60)
    eraser = Item.create("Eraser", 0.20)
    pencilSet = Item.compose("Pencil Set", pencil, ruler, eraser)
    box = Item.create("Box", 1.00)
    boxedPencilSet = Item.compose("Boxed Pencil Set ", box, pencilSet)
    boxedPencilSet.add(pencil)

    for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
        item.print()


if __name__ == "__main__":
    main()
