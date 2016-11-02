from builder import Builder

class TextBuilder(Builder):

    def __init__(self):
        self.__buffer = []

    def make_title(self, title):
        self.__buffer.append('=' * 20)
        self.__buffer.append('\n')
        self.__buffer.append('[' + title + ']\n')
        self.__buffer.append('\n')

    def make_string(self, string):
        self.__buffer.append('■' + string + '\n')
        self.__buffer.append('\n')

    def make_items(self, items):
        for item in items:
            self.__buffer.append('●' + item + '\n')
        self.__buffer.append('\n')

    def close(self):
        self.__buffer.append('=' * 20)

    def get_result(self):
        str = ""

        for buffer in self.__buffer:
            str += buffer

        return str
