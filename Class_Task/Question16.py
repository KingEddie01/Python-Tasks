def multiples():
    first_number = int(input("Enter number : "))
    second_number = int(input(" Enter number : "))

    for counter in range(1, first_number * second_number):
        if counter % first_number == 0 and counter % second_number == 0:
            print()
        print(counter)
        return


if __name__ == '__main__':
    multiples()
