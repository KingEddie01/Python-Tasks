def intercept(list1, list2):
    new_list = []
    for element in list1:
        if list2.__contains__(element):
            new_list.append(element)
    return tuple(set(new_list))


list1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 6, 9]
list2 = [1, 3, 4, 6, 6, 16, 78, 90, 21, 45]

result = intercept(list1, list2)
print(result)
