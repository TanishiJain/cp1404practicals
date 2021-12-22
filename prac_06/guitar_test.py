from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print("{} get age() - Expected 99. Got {}".format(gibson.name, gibson.get_age(), gibson.get_age()))
    print("{} is vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage(), gibson.is_vintage()))
    tester = Guitar("Tester", 1995, 3000)
    print("{} get age() - Expected 26. Got {}".format(tester.name, tester.get_age(), tester.get_age()))
    print("{} is vintage() - Expected False. Got {}".format(tester.name, tester.is_vintage(), tester.is_vintage()))


if __name__ == '__main__':
    main()