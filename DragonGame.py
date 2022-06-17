import random

import time

def displayIntro():
	print('''You are in the lands inhabited by dragons.
 	In front of you you see two caves. In one of them is a friendly dragon,
 	who is ready to share his treasures with you. In the second -
 	Greedy and hungry dragon that will eat you up in no time.''')

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you choose?(choose between 1 or 2)')
		cave = input()

	return cave

def checkCave(chosenCave):
	print('You are getting closer to cave...')
	time.sleep(2)
	print('Its darkness make you feel scary...')
	time.sleep(2)
	print('Huge dragon jump in front of you! He opens his mouse and...')
	print('...')
	time.sleep(2)
	print('...')
	time.sleep(2)
	print('...')
	time.sleep(2)
	print('...')
	time.sleep(2)
	print('...')
	time.sleep(2)
	print('...')
	time.sleep(7)

	friendlyCave = random.randint(1,2)

	if chosenCave == str(friendlyCave):
		print('...gives you all treasures!')
	else:
		print('...instantly eats you!')
# start
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print('Try tour best one more time! (yes or no)')
	playAgain = input()

input('press Enter to leave')