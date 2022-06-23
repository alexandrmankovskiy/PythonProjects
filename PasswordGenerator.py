import random

def getOptions(max):
	passLen = int(input('Enter the lenth of password'))
	incSym = input('Do you want to include symbols in your password? type y/n')
	incNum = input('Do you want to include numbers in your password? type y/n')
	incLet = input('Do you want to include letters in your password? type y/n')
	password = ' '
	if incNum == 'y' and incSym == 'y' and incLet == 'y':
		for i in range(passLen):
			random1 = random.randint(0, max)
			randSym = symlse[random.randint(0,len(symlse)-1)]
			randLet = letters[random.randint(0,len(letters)-1)]
			randomNum = numbers[random.randint(0,len(numbers)-1)]
			if random1 == 0:
				password = randSym + password
			elif random1 == 1:
				password = randLet + password
			else:
				password = randLet + password

	print(password)





symlse = '! @ # $ % ^ & ? * ( ) ] [ { } = - + _ /'.split()
letters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'.split()
numbers = '1 2 3 4 5 6 7 8 9 0'.split()
print('Hi, Alex, select options for ur passWords')
getOptions(3)


input()