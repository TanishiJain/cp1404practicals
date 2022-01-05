menu = """q)uit, c)hoose taxi, d)rive"""

from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

def main():
    current_taxi = None
    current_bill = 0
    print("Lets Drive!")
    print(menu)
    menu_input = input(">>>").lower()
    while menu_input != "q":
        if menu_input == "c":
            print("Texis available")
            print_taxi(taxis)
            input_taxi = int(input("Choose Taxi:"))
            try:
                current_taxi = taxis[input_taxi]
            except IndexError:
                print("Invalid Taxi Choice")

        elif menu_input == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how Far? "))
                current_taxi.drive(drive_distance)
                cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             cost))
                current_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(current_bill))
        print(menu)
        menu_input = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(current_bill))
    print("Taxis are now")
    print_taxi(taxis)

def print_taxi(taxis):
    for i , taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))



if __name__ == '__main__':
    main()