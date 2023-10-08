def fibonacci(digit):
    y = 0
    number = [0, 1]
    while y < digit:
        num = number[-1] + number[-2]
        if num < digit:
            number.append(num)
        y += 1
    for count in number:
        print(count, end=" ")


fibonacci(50)
