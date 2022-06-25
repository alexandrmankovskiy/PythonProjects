# tictactoe game
import random

def drawBoard(board):
	#Displays game board, fields which will be fild

	# "board" - is list of strings, forrendering game board
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def PlayersLatter():
	# Allows player input a letter
	# Returns list, in which players 
	letter = ''
	while not (letter == 'X' or letter == "O"):
		print('Choose X or O')
		letter = input().upper()

	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirst(): #Chooses who goes 1st
	if random.randint(0,1) == 1:
		return 'Computer'
	else:
		return 'Human'

def makeMove(board, letter, move): # makes move
	board[move] = letter

def isWinner(bo, le): # returns True if player won
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le))
def getBoardCopy(board):
	#Creates copy of game board for AI conculations
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

def isSpaceFree(board, move): # Returns True if free part is chosen
	return board[move] == ' '

def PlayerMove(board):
	#Allows player to make a move
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('Your next move?(1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, moveList): # Returns allowed move, including list of already done moves. Returns None, if there is no more posiible moves
	possibleMoves = []
	for i in moveList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None
def isBoardFull(board): # returns True if space is over
	for i in range(1,10):
		if isSpaceFree(board, i):
			return False
	return True

def ComputerMove(board, computerLetter):
	# including filled boards and comp letter
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter ='X'
	# The beginning of AI code
	# Checking if computer wins, making next move
	for i in range(1,10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, computerLetter, i)
			if isWinner(boardCopy, computerLetter):
				return i
	# Checking if player wins making next move, and block it
	for i in range(1,10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, playerLetter, i)
			if isWinner(boardCopy, playerLetter):
				return i
	# Trying to fit any of angls
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	# Trying to fit center
	if isSpaceFree(board, 5):
		return 5

	return chooseRandomMoveFromList(board, [2, 4, 6, 8])



print('Game Tictactoe!')

while True:
	# Reload of gaming board
	theBoard = [' '] * 10
	playerLetter, computerLetter = PlayersLatter()
	turn = whoGoesFirst()
	print('' + turn + ' goes first')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'Human':
			# Players turn.
			drawBoard(theBoard)
			move = PlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('YEAH! You won!!!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Draw!')
					break
				else:
					turn = 'Computer'
		else:
			# computers turn
			move = ComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('Computer won, you lost!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('Draw!')
					break
				else:
					turn = 'Human'

	print('Do you want to play again? (yes or no)')
	if not input().lower().startswith('y'):
			break