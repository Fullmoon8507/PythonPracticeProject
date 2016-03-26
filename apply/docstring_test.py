def echo(anything):
    'echoは、与えられた入力引数を返す'

    return anything

def print_if_true(thing, check):
    '''
    第２引数が真なら、第１引数を表示する
    処理内容：
        １：第２引数が真かどうかチェックする。
        ２：真なら第１引数を表示する。
    '''

    if check:
        print(thing)


if __name__ == "__main__":
    print(echo("test!"))
    print_if_true("It's true!", True)
