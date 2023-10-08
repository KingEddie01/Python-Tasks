def is_palindrome(word):
    if word.casefold() == word[:: -1].casefold():
        print("word is a palindrome")
        return True
    else:
        print("word is not a palindrome")
        return False


print(is_palindrome("hubby"))
