def name_multiples():
    Element = input("ENTER ELEMENT : ")
    n = int(input("enter number :  "))
    if n < 0:
        name_multiples()
    print(f"{Element}\n" * n)


if __name__ == '__main__':
    name_multiples()
