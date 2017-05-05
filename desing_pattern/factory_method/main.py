from idcard_factory import IDCardFactory


def main():
    factory = IDCardFactory()
    card1 = factory.create('稲葉浩志')
    card2 = factory.create('松本孝弘')
    card3 = factory.create('谷山紀章')
    card4 = factory.create('飯塚昌明')

    card1.use()
    card2.use()
    card3.use()
    card4.use()


if __name__ == "__main__":
    main()
