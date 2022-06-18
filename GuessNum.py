# Game Guess Number
import random

NumOfTryes = 0

print("Hello, name yourself: ")

Name = input()

def code():
    print(Name + ", enter range u want to guess from:")

    FirstNum = int(input("First num : "))
    SecondNum = int(input("Second num: "))

    RandomNumOfTryes = random.randint(5, 10)

    print(Name + ", you have " + str(RandomNumOfTryes) + " tryes")

    print("So, " + Name + " lets start, try to guess:")

    Integer = random.randint(FirstNum, SecondNum)

    print("Game started")

    for NumOfTryes in range(RandomNumOfTryes):
        answer = input()
        answer = int(answer)

        if answer < Integer:
            print("Your num is to small")

        if answer > Integer:
            print("Your num is too big")

        if answer == Integer:
            print("Your num is correct!")
            break

        NumOfTryes += NumOfTryes

        if NumOfTryes == RandomNumOfTryes:
            break
            print("Sorry " + Name + "u are out of tryes")
            print("The secret number was: " + Integer)

    if answer == Integer:
        NumOfTryes = str(NumOfTryes + 1)
        print("Congrast, " + Name + " u did it!. It took u " + NumOfTryes + " tryes!")
        print("Do you want to continue or exit? Type y/n")


yorn = 'yes'

while yorn == 'yes' or yorn == 'y':
    code()
    yorn = input()

input("Press ENter to leave...")
