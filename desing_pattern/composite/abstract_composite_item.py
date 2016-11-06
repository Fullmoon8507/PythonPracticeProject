from abstract_item import AbstractItem


class AbstractCompositeItem(AbstractItem):

    def __init__(self, *items):
        self.children = []
        if items:
            self.add(*items)

    def add(self, first, *items):
        self.children.append(first)
        if items:
            self.children.extend(items)

    def remove(self, item):
        self.children.remove(item)
    
    def __iter__(self):
        return iter(self.children)
