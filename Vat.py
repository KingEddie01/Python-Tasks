def vat():
    try:
        amount = float(input("Enter the price of the item : "))
        if amount < 0:
            print(" Enter a valid amount")
            vat()
        Vat = float(input("Enter the Vat percentage: "))
        if Vat < 0:
            print("Invalid input")
            vat()
        vat_amount = amount * (Vat / 100)
        final_amount = amount + vat_amount
        print(final_amount)
    except ValueError:
        print("Enter a Valid input")
        vat()


if __name__ == '__main__':
    vat()
