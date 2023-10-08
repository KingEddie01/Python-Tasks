Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]


def share(start, end):
    new_list = []
    step = 3
    for letter in range(step):
        new_list.append(start[letter::step])
    return new_list


print(share(Letters, 3))
