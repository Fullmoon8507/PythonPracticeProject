animal = 'fruitbat'

def change_local():
    animal = 'wombat'
    print('local:', locals())

if __name__ == "__main__":
    print(animal)
    change_local()
    print('globals', globals())
    print(animal)
