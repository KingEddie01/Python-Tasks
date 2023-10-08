def divisible_7():
    for numbers in range(1500, 2701):
        if numbers % 7 == 0 and numbers % 5 == 0:
            print(numbers)


if __name__ == '__main__':
    divisible_7()
