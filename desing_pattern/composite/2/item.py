import sys
import itertools


class Item:

    def __init__(self, name, *items, price=0.00):
        self.name = name
        self.price = price
        self.children = []
        if items:
            self.add(*items)

    @classmethod
    def create(Class, name, price):
        return Item(name, price=price)

    @classmethod
    def compose(Class, name, *items):
        return Item(name, *items)

    def make_item(name, price):
        return Item(name, price=price)

    def make_composite(name, *items):
        return Item(name, *items)

    @property
    def composite(self):
        return bool(self.children)

    def add(self, first, *items):
        self.children.extend(itertools.chain((first,), items))

    def remove(self, item):
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)

    @property
    def price(self):
        return (sum(item.price for item in self) if self.children else self.__price)

    @price.setter
    def price(self, price):
        self.__price = price

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name),file=file)
        for child in self:
            child.print(indent + " ")
