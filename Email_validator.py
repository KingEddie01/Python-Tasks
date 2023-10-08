def Email_validator(email):
    emails = []
    SpecialCharacters = ('~', '!', '@', '#', '$', '%', '^', '&', '*', '()', '-', '_', '+', '=', '{}', '[]', '|', '\';',
                         ':', '"', '<>', '.', '/', '?')
    condition = True
    for element in email:
        if element.startswith(SpecialCharacters):
            print("invalid email")
            Email_validator()
        if element.count('@') > 1:
            print("invalid email")
            Email_validator()
        if element.endswith(SpecialCharacters):
            print("Invalid email")
            Email_validator()
        if condition:
            print("Email is valid")
        emails.append(element)
        return emails


if __name__ == '__main__':
    Email_validator(print(list))
