# Game Guess Number
import random

NumOfTryes = 0

print("Hello, name yourself: ")

Name = input()

print(Name + ", enter range u want to guess from:")

FirstNum = input("First num : ")
SeconfNum = input("Second num: ")

RandomNumOfTryes = random.randint(5,10)

print(Name + ", you have " + RandomNumOfTryes + " tryes")

print("So, " + Name + " lets start, try to guess:")

Integer = random.randint(FirstNum, SeconfNum)

for NumOfTryes in range(RandomNumOfTryes):
	print("Game started")
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
	print("Congrast, " + Name + " u did it!. It took u " + NumOfTryes + "tryes!")

input("Press ENETR to leave...")
