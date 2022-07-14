import random
import sys

def filters(passLen, incSym, incNum, incLet):

	for j in range(16):
		password = []
		if incNum == 'y' and incSym == 'y' and incLet == 'y':
				for i in range(passLen):
					random1 = random.randint(0, 2)
					randSym = symlse[random.randint(0,len(symlse)-1)]
					randLet = letters[random.randint(0,len(letters)-1)]
					randomNum = numbers[random.randint(0,len(numbers)-1)]
					if random1 == 0:
						password.append(randSym)
					elif random1 == 1:
						password.a16ppend(randLet)
					else:
						password.append(randomNum)
					if (randSym not in password) or (randLet not in password) or (randomNum not in password):
						password = []
						i -= 1
					continue
		elif incNum == 'n' and incSym == 'y' and incLet == 'y':
				for i in range(passLen):
					random1 = random.randint(0, 1)
					randSym = symlse[random.randint(0,len(symlse)-1)]
					randLet = letters[random.randint(0,len(letters)-1)]
					if random1 == 0:
						password.append(randSym)
					elif random1 == 1:
						password.append(randLet)
					if (randSym not in password) or (randLet not in password):
						password = []
						i -= 1
						continue
		elif incNum == 'y' and incSym == 'n' and incLet == 'y':
				for i in range(passLen):
					random1 = random.randint(0, 1)
					randLet = letters[random.randint(0,len(letters)-1)]
					randomNum = numbers[random.randint(0,len(numbers)-1)]
					if random1 == 0:
						password.append(randomNum)
					elif random1 == 1:
						password.append(randLet)
					if (randLet not in password) or (randomNum not in password):
						password = []
						i -= 1
						continue
		elif incNum == 'y' and incSym == 'y' and incLet == 'n':
				for i in range(passLen):
					random1 = random.randint(0, 1)
					randSym = symlse[random.randint(0,len(symlse)-1)]
					randomNum = numbers[random.randint(0,len(numbers)-1)]
					if random1 == 0:
						password.append(randomNum)
					elif random1 == 1:
						password.append(randSym)
					if (randSym not in password) or (randomNum not in password):
						password = []
						i -= 1
						continue
		elif incNum == 'y' and incSym == 'n' and incLet == 'n':
				for i in range(passLen):
					randomNum = numbers[random.randint(0,len(numbers)-1)]
					password.append(randomNum)			
		elif incNum == 'n' and incSym == 'y' and incLet == 'n':
				for i in range(passLen):
					randSym = symlse[random.randint(0,len(symlse)-1)]
					password.append(randSym)
		elif incNum == 'n' and incSym == 'n' and incLet == 'y':
				for i in range(passLen):
					randLet = letters[random.randint(0,len(letters)-1)]
					password.append(randLet)
		else:
			print('Try again! Type as an example shows!!!')
			print()
			break
		if j < 9:
			extraspace='  '
		else:
			extraspace=' '
		print('%s)%s%s' % (j+1,extraspace,''.join(password)))
extraspace = ''
symlse = '! @ # $ % ^ & ? * ( ) = - +'.split()
letters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A D S F G H J K L Z X C V B N M'.split()
numbers = '1 2 3 4 5 6 7 8 9 0'.split()
print('Welcome to password generator, Alex!')
print()
while True:
	print('Enter: password lenth(8 to 64) | include symbols(y/n) | include numbers(y/n) | include letters(y/n)')
	print('Example: 16 n y y')
	print()
	filterpar = input().lower().split()
	if filterpar[0].isdigit()==True and (int(filterpar[0]) > 7 and int(filterpar[0]) < 65) and ((filterpar[1] == 'y' or filterpar[1] == 'n') and (filterpar[2] == 'y' or filterpar[2] == 'n') and (filterpar[3] == 'y' or filterpar[3] == 'n')):
		print('')
		filters(int(filterpar[0]), filterpar[1], filterpar[2], filterpar[3])
		if input('Do you want to generate more? Press Enter to continue or type "n" to leave: ').lower().startswith('n'):
			sys.exit()
		else:
			continue
	else:
		print('Plaese, eneter as an example shows: 16 y n y')

