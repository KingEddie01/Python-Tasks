List2 = [5, 4, 9, 7, 2, 0]


def sum_list(list1, value):
    List3 = List2
    for num in range(len(List2) - 1):
        for number in range(1, len(List3) - 1):
            if List2[num] + List3[number] == value:
                return [num, number]


print(sum_list(List2, 16))
