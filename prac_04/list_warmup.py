def main():
    numbers = [3,1,4,1,5,9,2]
    numbers[0] = "10"
    numbers[-1] = 1
    print(numbers[-5:7])
    if 9 in numbers:
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()

