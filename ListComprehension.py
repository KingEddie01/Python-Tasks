number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(n):
    return n ** 2


num = [counter for counter in number if square(counter)]
print(list(map(square, number)))


def even(n):
    if n % 2 == 0:
        return n


digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number1 = [counter for counter in digit if even(counter)]

print(list(filter(even, digit)))
