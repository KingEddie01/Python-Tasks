def credit_Card_Validator():

    card_details = []
    converted_details = []
    card_number = input("Hello Kindly enter Cards details to verify : ")
    if card_number.isdigit():
        for numbers in card_number:
            card_details.append(numbers)
        converted_details = [eval(num) for num in card_details]
        sum_digit1 = 0
        sum_digit2 = 0
        if len(converted_details) >= 13 or len(converted_details) <= 16:
            digit = len(converted_details) - 2
            while digit >= 0:
                new_detail = converted_details[digit] * 2
                if new_detail > 9:
                    sum_digit = int(new_detail / 10) + (new_detail % 10)
                    sum_digit1 += sum_digit
                    digit -= 2
                else:
                    sum_digit2 += new_detail
                    digit -= 2
            finalTotal = sum_digit1 + sum_digit2

            second_Sum = 0
            counter = len(converted_details) - 1
            while counter > 0:
                second_Sum += converted_details[counter]
                counter -= 2
                sum_Total = 0
                sum_Total = finalTotal + second_Sum
            if converted_details[0] == 4 and sum_Total % 10 == 0:
                print(f"*********************************************************\n** CREDIT CARD TYPE : VISA CARD "
                      f"\n** CREDIT CARD NUMBER : {card_number}\n** CREDIT CARD LENGTH : {len(card_number)}\n** "
                      f"CREDIT CARD VALIDITY STATUS : VALID"
                      f"\n*********************************************************")

            elif converted_details[0] == 5 and sum_Total % 10 == 0:
                print(f"*********************************************************\n** CREDIT "
                      f"CARD TYPE : MASTER CARD \n** CREDIT CARD NUMBER : {card_number}\n** CREDIT CARD LEN"
                      f"GTH : {len(card_number)}\n** CREDIT CARD VALIDITY STATUS : VALID"
                      f"\n*********************************************************")

            elif converted_details[0] == 3 and converted_details[1] == 7 and sum_Total % 10 == 0:
                print(f"*********************************************************\n** CREDIT "
                      f"CARD TYPE : AMERICAN EXPRESS CARD \n** CREDIT CARD NUMBER : {card_number}\n** CREDIT CARD "
                      f"LENGTH : {len(card_number)}\n** CREDIT CARD VALIDITY STATUS : VALID"
                      f"\n*********************************************************")
            elif converted_details[0] == 6 and sum_Total % 10 == 0:
                print(f"*********************************************************\n** CREDIT "
                      f"CARD TYPE : DISCOVER CARD \n** CREDIT CARD NUMBER : {card_number}\n** CREDIT CARD LEN"
                      f"GTH : {len(card_number)}\n** CREDIT CARD VALIDITY STATUS : VALID"
                      f"\n*********************************************************")
            else:
                print(f"CREDIT CARD IS INVALID")
                credit_Card_Validator()
    else:
        print("ENTER A VALID CREDIT CARD ")
        credit_Card_Validator()


if __name__ == '__main__':
    credit_Card_Validator()
