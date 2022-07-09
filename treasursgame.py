import random
import math
import sys

def getNewBoard(): #Create structured data of game field
    board = []
    for x in range(60): #Main list of 60 lists
        board.append([])
        for y in range(15):#Every list in main list consists 15 subsymbolic strings
            #For creation the ocean using different symbols, to make it more real
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board): #Display the structured data of gaming field
    tensDigitsLine = ' ' #Creates a space for numbers down the left side of the field
    for i in range(1, 6):
        tensDigitsLine += (' '* 9) + str(i)
    #Display digits in upper part of a field
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()
    #Display every of 15 rows
    for row in range(15):
        #We need to add a extra space to single meaning numbers
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        
        #Create a string for this row in game board
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]
        
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))
    #Display numbers in bottom
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

theBoard = getNewBoard()
drawBoard(theBoard)
