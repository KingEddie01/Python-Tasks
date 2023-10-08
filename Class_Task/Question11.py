import re


def vowels():
    Letter = input(" Enter a letter")
    if re.search(r'[a e i o u]', Letter):
        print("is a vowel")
    else:
        print("not a vowel ")


vowels()
