import random

def getOptions():
	max1 = 2
	max2 = 1
	passLen = int(input('Enter the lenth of password: '))
	incSym = input('Do you want to include symbols in your password? type y/n ').lower()
	incNum = input('Do you want to include numbers in your password? type y/n ').lower()
	incLet = input('Do you want to include letters in your password? type y/n ').lower()
	password = ' '
	if passLen > 7:
		if incNum == 'y' and incSym == 'y' and incLet == 'y':
			for i in range(passLen):
				random1 = random.randint(0, max1)
				randSym = symlse[random.randint(0,len(symlse)-1)]
				randLet = letters[random.randint(0,len(letters)-1)]
				randomNum = numbers[random.randint(0,len(numbers)-1)]
				if random1 == 0:
					password = randSym + password
				elif random1 == 1:
					password = randLet + password
				else:
					password = randomNum + password
		elif incNum == 'n' and incSym == 'y' and incLet == 'y':
			for i in range(passLen):
				random1 = random.randint(0, max2)
				randSym = symlse[random.randint(0,len(symlse)-1)]
				randLet = letters[random.randint(0,len(letters)-1)]
				if random1 == 0:
					password = randSym + password
				elif random1 == 1:
					password = randLet + password
		elif incNum == 'y' and incSym == 'n' and incLet == 'y':
			for i in range(passLen):
				random1 = random.randint(0, max2)
				randLet = letters[random.randint(0,len(letters)-1)]
				randomNum = numbers[random.randint(0,len(numbers)-1)]
				if random1 == 0:
					password = randomNum + password
				elif random1 == 1:
					password = randLet + password
		elif incNum == 'y' and incSym == 'y' and incLet == 'n':
			for i in range(passLen):
				random1 = random.randint(0, max2)
				randSym = symlse[random.randint(0,len(symlse)-1)]
				randomNum = numbers[random.randint(0,len(numbers)-1)]
				if random1 == 0:
					password = randomNum + password
				elif random1 == 1:
					password = randSym + password
		elif incNum == 'y' and incSym == 'n' and incLet == 'n':
			for i in range(passLen):
				randomNum = numbers[random.randint(0,len(numbers)-1)]
				password = randomNum + password			
		elif incNum == 'n' and incSym == 'y' and incLet == 'n':
			for i in range(passLen):
				randSym = symlse[random.randint(0,len(symlse)-1)]
				password = randSym + password
		elif incNum == 'n' and incSym == 'n' and incLet == 'y':
			for i in range(passLen):
				randLet = letters[random.randint(0,len(letters)-1)]
				password = randLet + password		
	else:
				print('Sorry, the lenth of your password can not be lower 8!')

	print(password)





symlse = '! @ # $ % ^ & ? * ( ) ] [ { } = - + _ /'.split()
letters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A D S F G H J K L Z X C V B N M'.split()
numbers = '1 2 3 4 5 6 7 8 9 0'.split()

print('Hi, Alex, select options for ur passWords')
getOptions()


input()