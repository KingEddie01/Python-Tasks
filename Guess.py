def Random_number():
    number = int(input("Enter a number from 1 - 10 : "))
    while number == 7:
        print("you have won")
        return
    else:
        if -1 < number <= 4:
            print("Number too low, try again")
            Random_number()
        elif 11 > number > 4:
            print("Number too high, try again")
            Random_number()


if __name__ == '__main__':
    Random_number()
