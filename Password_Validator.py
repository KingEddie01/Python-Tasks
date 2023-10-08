import re


def Password_Validator():
    password = input("Enter your password : ")
    Special_Character = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    check = re.compile(Special_Character)

    match = re.search(check, password)

    if match:
        print("Password is valid.")
    else:
        print("Password invalid!")
        Password_Validator()


if __name__ == '__main__':
    Password_Validator()
