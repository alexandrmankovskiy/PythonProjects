import random
import time
i = 0
heads = 0
print('Hello, im going to flip a coin for as times as u wish! than u try to guess!')
time.sleep(2)
name = input('Eneter your name first: ')
def Asking():
	sideOfCoin = input('Enter side u wonna track (heads or tails h/t): ')
	if sideOfCoin == 'h':
		sideOfCoin = 'heads'
	if sideOfCoin == 't':
		sideOfCoin = 'tails'
	numOfFlips = int(input('Enter number of flips u want to perform: '))
	tryToGuess = int(input('Enter aproximate number of ' + sideOfCoin +' tyrned: '))
	print('Ok, ' + name + ' lets strart')
	print('doing calculations.../')
	time.sleep(2)
	while i < numOfFlips:
		if random.randint(0,1) == 1:
			heads = heads + 1
	if sideOfCoin == 'heads':
		if tryToGuess == heads:
			print('Congrats, ' + name + 'Alex')
		else:
			if tryToGuess < heads:
				print('you almost got it! try higher next time! The result is:' + str(heads))
			else:
				print('you almost got it! try lower next time! The result is:' + str(heads))
	if sideOfCoin == 'tails':
		if tryToGuess < heads:
				print('you almost got it! try higher next time! The result is:' + str(numOfFlips-heads))
		else:
				print('you almost got it! try lower next time! The result is:' + str(numOfFlips-heads))
        i = i + 1

        
plyaAgain = 'yes'
while plyaAgain != 'n':
	Asking()
	plyaAgain = input('do you want to play again? Type "n" if u want to exit')

input('Press Enter to leave')

