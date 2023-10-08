e_list = []
for number in range(10):
    e_list += [number]
print(e_list)

letter = []
letter += 'Edmund'

print(letter[0])
print(letter)

first_list = [1, 2, 3, 4, 5]
second_list = (6, 7, 8, 9, 10)
first_list += second_list
print(first_list)


# for num in range(len(new_list)):
#     print(f'{num} : {new_list[num]}', )


def cube_list(values):
    for counter in range(len(values)):
        values[counter] **= 3
        print(values[counter], end=' ')


digits = [3, 2, 1, 4, 5]
cube_list(digits)
print()

time = (9, 16, 1)
seconds = time[0] * 3600 + time[1] * 60 + time[2] * 1
print('Total seconds is  : ', seconds)

print()

tuple1 = ('age', 'grade', 'male')
tuple2 = ([2023, 17],)
tuple1 += tuple2
print(tuple1)

print()
number1 = 10
number2 = 20
number1, number2 = number2, number1
print(f'{number1} {number2}')
