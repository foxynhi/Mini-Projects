NUMBER_OF_DIGITS = 10
def main():
    print('Soroban - The Japanese Abacus')
    number = 0

    while True:
        while True:
            print('Enter a number, "quit", or a stream of up/down letters.')
            action = input('> ')

            if action.isdecimal() and int(action) < 10000000000:
                number = int(action)
                break

            action = action.lower()
            if action == 'quit':
                quit()
                
            actionList = list('qwertyuiopasdfghjkl;')
            if set(action) <= set(actionList):
                for i in action:
                    if i == 'q':
                        number += 1000000000
                    elif i == 'w':
                        number += 100000000
                    elif i == 'e':
                        number += 10000000
                    elif i == 'r':
                        number += 1000000
                    elif i == 't':
                        number += 100000
                    elif i == 'y':
                        number += 10000
                    elif i == 'u':
                        number += 1000
                    elif i == 'i':
                        number += 100
                    elif i == 'o':
                        number += 10
                    elif i == 'p':
                        number += 1
                    elif i == 'a':
                        number -= 1000000000
                    elif i == 's':
                        number -= 100000000
                    elif i == 'd':
                        number -= 10000000
                    elif i == 'f':
                        number -= 1000000
                    elif i == 'g':
                        number -= 100000
                    elif i == 'h':
                        number -= 10000
                    elif i == 'j':
                        number -= 1000
                    elif i == 'k':
                        number -= 100
                    elif i == 'l':
                        number -= 10
                    elif i == ';':
                        number -= 1
                if number < 0 :
                    number = 0
                elif number > 9999999999:
                    number = 9999999999
                    
                break

        displaySoroban(number)
        

def displaySoroban(number):    
    hasBead = []
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

    #TOP
    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '01234')

    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '56789')

    #BOTTOM
    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '12346789')

    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '234789')

    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '034589')

    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '014569')

    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '012567')

    for n in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[n] in '01235678')

    abacusChar = []
    for i in hasBead:
        abacusChar.append('O' if i is True else '|')

    for n in range(NUMBER_OF_DIGITS):
        abacusChar.append(numberList[n])

    print('''
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+
  +q  w  e  r  t  y  u  i  o  p
  -a  s  d  f  g  h  j  k  l  ;'''.format(*abacusChar))


if __name__ == '__main__':
    main()