from taxi import Taxi


def main():
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print(prius)
    prius.start_fare()
    prius.drive(100)
    print(prius)


if __name__ == '__main__':
    main()