import sys
import itertools


class Item:

    def __init__(self, id):
        self.id = id
        self.parent = []
        self.children_number = []
        self.children = []

    @classmethod
    def create(Class, id):
        return Item(id)

    def addChildren(self, *items):
        for item in items:
            self.children_number.append(item[0])
            self.children.append(item[1])

    def addParent(self, *items):
        self.parent.extend(itertools.chain(items))

    def printChildren(self, indent="", file=sys.stdout):
        if bool(self.children):
            print("{}{}".format(indent, self.id),file=file, end= " ")
            print(self.children_number, file=sys.stdout)
        else:
            print("{}{}".format(indent, self.id),file=file)

        for child in self.children:
            child.printChildren(indent + "  ")

    def printParent(self, indent="", file=sys.stdout):
        print("{}{}".format(indent, self.id),file=file)
        for child in self.parent:
            child.printParent(indent + "  ")

    #@classmethod
    #def compose(Class, name, *items):
    #    return Item(name, *items)

    #def make_item(name, price):
    #    return Item(name, price=price)

    #def make_composite(name, *items):
    #    return Item(name, *items)

    #@property
    #def composite(self):
    #    return bool(self.children)

    #def remove(self, item):
    #    self.children.remove(item)

    #def __iter__(self):
    #    return iter(self.children)

    #@property
    #def price(self):
    #    return (sum(item.price for item in self) if self.children else self.__price)

    #@price.setter
    #def price(self, price):
    #    self.__price = price

