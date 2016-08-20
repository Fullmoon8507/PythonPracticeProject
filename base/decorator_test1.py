'''
Created on 2016/08/20

@author: User
'''


def document_it(func):

    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


@document_it
def add_ints(a, b):
    return a + b

if __name__ == '__main__':
    # デコレータを使用しない場合
    # cooler_add_ints = document_it(add_ints)
    # cooler_add_ints(3, 5)
    # print()

    # デコレータを使用する場合
    add_ints(3, 5)
