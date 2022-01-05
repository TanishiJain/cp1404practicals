from unreliable_car import Unreliable_car


def main():
    bad_car = Unreliable_car("Bad car", 100,1)
    good_car = Unreliable_car("Good car",100,99)
    bad_car.drive(40)
    good_car.drive(50)
    print(bad_car)
    print(good_car)


if __name__ == '__main__':
    main()