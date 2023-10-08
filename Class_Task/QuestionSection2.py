def test_data():
    new_color = []
    color_list_1 = {"white", "Black", "Red"}
    color_list_2 = {"Red", "Green"}

    for element in color_list_1:
        if not element in color_list_2:
            new_color.append(element)
    print(new_color)


if __name__ == '__main__':
    test_data()
