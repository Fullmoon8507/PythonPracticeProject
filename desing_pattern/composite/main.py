from simple_item import SimpleItem
from composite_item import CompositeItem


def main():
    pencil = SimpleItem("Pencil", 0.40)
    ruler = SimpleItem("Ruler", 1.60)
    eraser = SimpleItem("Eraser", 0.20)
    pencilSet = CompositeItem("Pencil Set", pencil, ruler, eraser)
    box = SimpleItem("Box", 1.00)
    boxedPencilSet = CompositeItem("Boxed Pencil Set", box, pencilSet)
    boxedPencilSet.add(pencil)

    for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
        item.print()


if __name__ == "__main__":
    main()
