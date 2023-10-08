while True:
    try:
        num1, num2 = eval(input("Enter number seperated by comma : "))
        result = num1 / num2
        print(result)
    except SyntaxError:
        print("You cannot divide by zero")
    except ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        print("Thank you for using muy calculator")
    finally:
        print("Everything is well")
