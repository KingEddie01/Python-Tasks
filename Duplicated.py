duplicate = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]


def digit(selector):
    new_digit = []
    for element in selector:
        if element not in new_digit:
            new_digit += [element]
            return new_digit


print(digit(duplicate))

select = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
select = set(select)
select = list(select)
print(select)

counted = [2, 2, 4, 5, 6, 7, 8, 34, 65, 50, 120, 40]


def box(counted):
    counter = 0
    for number in counted:
        counter += 1
        return counter


print(box(counted))
