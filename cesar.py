import sys
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do u want to crypt or uncrypt? c/u')
        mode = input().lower()
        if mode in ['c','u','crupt','uncrypt']:
            return mode
        else:
            print('Type: "crypt" or "uncrypt" or "u" or "c" (c-crypt)')

def getMessage():
    print('Enter text:')
    return input()

def getKey():
    key = 0
    while True:
        print(f'Enter key for encryption (1-{MAX_KEY_SIZE})')
        key = int(input())

        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
        else:
            print(f'Enter key for encryption (1-{MAX_KEY_SIZE})')

def ENCRYPTION(mode, message, key):
    if mode[0] == 'u':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]
    return translated
while True:
    mode = getMode()
    message = getMessage()
    key = getKey()
    print('Converted text:')
    print(ENCRYPTION(mode, message, key))
    print('Press Enter repeate... or type "exit" to leave')
    if input().lower().startswith('e'):
        sys.exit()