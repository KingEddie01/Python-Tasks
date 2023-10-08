def divide_or_square(number):
    if number % 5 == 0:
        square_root = number**0.5
        return square_root
    elif number % 5 != 0:
        remainder = number % 5
        return remainder


print(f"{divide_or_square(10): .2f}")
            