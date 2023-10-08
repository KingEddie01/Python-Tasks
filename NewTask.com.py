def odd_number(number):
    counter = 0
    while counter < len(number):
        if number[counter] % 2 == 1:
            highest = number[counter]
            
            counter += 1

        return highest

    hr = [9, 3, 7, 46, 20, 10, 45, 98]

    tr = odd_number(hr)
    print(tr)










































