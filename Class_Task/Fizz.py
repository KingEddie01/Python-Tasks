def Fizz():
    for number in range(1, 51):
        if number % 3 == 0 and number % 5 == 0:
            print("FIZZ BUZZ")
            continue
        elif number % 3 == 0:
            print("FIZZ")
        elif number % 5 == 0:
            print("BUZZ")
        else:
            print(number)


if __name__ == '__main__':
    Fizz()
