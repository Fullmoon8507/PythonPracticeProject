def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

if __name__ == "__main__":
    print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
