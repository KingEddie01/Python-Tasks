import string


def password_check():
    Password = input("Enter your password : ")
    SpecialCharacters = string.punctuation

    condition = True

    if len(Password) < 8:
        print("The password length is below 8")
        password_check()

    if not any(char.isdigit() for char in Password):
        print('Password should have at least one number')
        password_check()

    if not any(char.isupper() for char in Password):
        print('Password should have at least one uppercase letter')
        password_check()

    if not any(char.islower() for char in Password):
        print('Password should have at least one lowercase letter')
        password_check()

    if not any(char in SpecialCharacters for char in Password):
        print('Password should have at least one special character')
        password_check()
    if condition:
        print("Valid Password")
        return


if __name__ == '__main__':
    password_check()
