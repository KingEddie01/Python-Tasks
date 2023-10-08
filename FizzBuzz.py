def Fizz_Buzz():
    for number in range(1, 1001):
        if number % 3 == 0 and number % 5 == 0:
            print("FIZZ BUZZ")
            continue
        if number % 3 == 0:
            print("FIZZ")
        elif number % 5 == 0:
            print("BUZZ")
        else:
            print(number)


if __name__ == '__main__':
    Fizz_Buzz()
