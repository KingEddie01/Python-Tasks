def divisor(a, b):
    number = max(a, b)
    number1 = min(a, b)
    for digit in range(number1, number):
        if number1 % digit == 0 and number % digit == 0:
            print(digit)
            return





if __name__ == '__main__':
    divisor()
