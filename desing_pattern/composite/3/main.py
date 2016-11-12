from item import Item


def main():
    top = Item.create("0001")

    node1 = Item.create("0011")
    node1.addParent(top)

    node2 = Item.create("0012")
    node2.addParent(top)

    node3 =Item.create("0021")
    node3.addParent(node1)

    node1.addChildren(("01", node3))
    top.addChildren(("01", node1), ("02", node2))
    
    top.printChildren()
    print("")

    node3.printParent()
    print("")


if __name__ == "__main__":
    main()
