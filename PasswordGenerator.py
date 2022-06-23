import random

def getOptions(max):
	passLen = int(input('Enter the lenth of password'))
	incSym = input('Do you want to include symbols in your password? type y/n')
	incNum = input('Do you want to include numbers in your password? type y/n')
	incLet = input('Do you want to include letters in your password? type y/n')
	password = ' ' * passLen
	if incNum == 'y' and incSym == 'y' and incLet == 'y':
		for i in range(passLen):
			random1 = random.randint(0, max)
			randSym = symlse[random.randint(0,len(symlse))]
			randLet = letters[random.randint(0,len(letters))]
			randomNum = numbers[random.randint(0,len(numbers))]
			if random == 0:
				password = password[:i] + randSym + password[i+1:]
			elif random == 1:
				password = password[:i] + randLet + password[i+1:]
			else:
				password = password[:i] + randLet + password[i+1:]

	return password





symlse = '! @ # $ % ^ & ? * ( ) ] [ { } = - + _ /'.split()
letters = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'.split()
numbers = '1 2 3 4 5 6 7 8 9 0'.split()
print('Hi, Alex, select options for ur passWords')
getOptions(3)


input()