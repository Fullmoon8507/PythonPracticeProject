animal = 'fruitbat'

def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

if __name__ == "__main__":
    print(animal)
    change_and_print_global()
    print(animal)
