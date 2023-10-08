def question1():
    studentNumber = []
    prompt1 = int(input("How many student do you have ?  "))
    if prompt1 < 0:
        print("Number is invalid!")
        question1()

    prompt2 = int(input("How many subject do they offer ? "))
    if prompt2 > 0:
        print()
        print("Saving>>>>>>>>>>>>>>""\nSaved Successfully")
    else:
        print("Number is invalid!")

    print()

    for counter in range(1, prompt1 + 1):
        for number in range(1, prompt2 + 1):
            print(f"Entering Score for student{counter}")
            score1 = int(input(f"Enter score for subject{number} : "))
            if score1 == range(1, 101):
                studentNumber.append(score1)
                print("Saving>>>>>>>>>>>>>>>>>>""\nSaved Successfully")
            print()
        counter += 1
    print("=======================================================================")
    print(f"CLASS SUMMARY - {prompt2} SUBJECTS")
    print("=======================================================================")
    print("STUDENT\t\t", end=" ")
    for num in range(1, prompt2 + 1):
        print(f"SUB{num}\t", end=" ")
    print(f"TOT\t AVG\t POS", end=" ")


if __name__ == '__main__':
    question1()
