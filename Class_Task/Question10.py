def first2_characters_multiple():
    word = []
    Element = input("Enter element")
    n = int(input(" Enter number : "))
    if n < 0:
        first2_characters_multiple()
        for letter in Element:
            word.append(letter)
        for counter in len(word):
            if counter <= 1:
                print(f"{word[counter]}")


if __name__ == '__main__':
    first2_characters_multiple()
