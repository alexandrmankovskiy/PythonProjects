import random
import math
import sys
from turtle import distance
import pyfiglet


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

def getRandomChests(numChests):#Generating random treasures chests
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0,59), random.randint(0,14)]
        if newChest not in chests: #make sure that chest is not generated yet
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    #Returns True, if coordinates possible in on a board. False if not
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    #change structure of field data, using symbol of hydrolokator. Delete chests
    # with treasurs from the list with chest, as soon as they ve been found.Return False, if its unaccessible move.
    # In oher case, return string with results of this move
    smallestDistance = 100 #all chests will be located closer, than 100 points
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - y) + (cy - y)*(cy - y))
        if distance < smallestDistance: # we need closest shest with treasures
            smallestDistance = distance
        smallestDistance = round(smallestDistance)
        if smallestDistance == 0:
            # coordinates went straight for treasurs chest
            chests.remove([x],[y])
            return 'You have found chest with treasurs !'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return f'Chest with treasurs has been detected on a {smallestDistance} distance'
            else:
                board[x][y] = 'X'
                return 'Locator did not detect treasurs. All chests are not in the feild of view'

def enterPlayersMove(previousMoves):
    print('Where to put locator?(coordinates: 0-59 0-14)(or type "exit to leave")')
    while True:
        move = input()
        if move.lower() == 'exit':
            print('Thznk you for playing!')
            sys.exit()
        
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('U have already tryed this!')
                continue
            return [int(move[0]), int(move[1])]
        print('Enter number from 0 to 59,then space, than nuber from 0 to 14')

def showInstructions():		
	print('''Инструктаж:
Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
гидролокаторов найти три сундука с сокровищами в затонувших судах на дне океана.
Но гидролокаторы очень просты и определяют только расстояние, но не направление.				
Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано
число, обозначающее, на каком расстоянии находится ближайший сундук. Или будет
показана буква Х, обозначающая, что сундук в области действия гидролокатора не 
обнаружен. На карте ниже метки C - это сундуки. 
Цифра 3 обозначает, что ближайший сундук находится на отдалении в 3 единицы.

                            1         2         3
                  012345678901234567890123456789012

                0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
                3 ````````~~~`````~~~`~`````~`~``~` 3
                4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                  012345678901234567890123456789012		
                            1         2         3
(Во время игры сундуки на карте не обозначаются!)

Нажмите клавишу Enter, чтобы продолжить...''')
	input()

	print('''Если гидролокатор опущен прямо на сундук, вы сможете поднять
сундук. Другие гидролокаторы обновят данные о расположении ближайшего сундука.
Сундуки ниже находятся вне диапазона локатора, поэтому отображается буква X.		

                            1         2         3
                  012345678901234567890123456789012		
		
                0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
                3 ````````~~~`````~~~`~`````~`~``~` 3
                4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                  012345678901234567890123456789012
                            1         2         3

Сундуки с сокровищами не перемещаются. Гидролокаторы определяют сундуки
на расстоянии до 9 единиц. Попробуйте поднять все 3 сундука до того, как все
гидролокаторы будут опущены на дно. Удачи!		

Нажмите клавишу Enter, чтобы продолжить...''')
	input()

enterence = pyfiglet.figlet_format('Treasurs Game !')
print(enterence)
print()
print('do you wonna see instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    # configuring game
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []
    chestslen = len(theChests)

    while sonarDevices > 0:
        #display sonar devices and chests with treasurs
        print(f'Sonar devices left: {sonarDevices} Chests to find: {chestslen}')
        x, y = enterPlayersMove(previousMoves)
        previousMoves.append([x,y])
        moveresult = makeMove(theBoard, theChests, x, y)
        if moveresult == False:
            continue
        else:
            if moveresult == 'You have found chest with treasurs !':
                #update all sonars, displayed on the board
                for x, y in previousMoves:
                    makeMove(theBoard, theChests,x,y)
            drawBoard(theBoard)
            print(moveresult)
        
        if(len(theChests) == 0):
            print('You have found all chests with treasurs! CONGRATS!!!')
            break
        sonarDevices -= 1
        if sonarDevices == 0:
            print('You are out of the sonars, you lost!')
            print(f'You did not find chests on: {x}, {y}')
        print('Do u want to play again? Yes/No')
        if input().lower().startswith('n'):
            sys.exit()