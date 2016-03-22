def print_args(*args):
    print('Positional argument tuple', args)

if __name__ == "__main__":
    print_args()
    print_args(3, 2, 1, 'wait!', 'uh...')
