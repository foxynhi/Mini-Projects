import random

print('''This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this.) The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')

input('Press Enter to begin...\n')

player1 = input('Human player 1, enter your name: ')
player2 = input('Human player 2, enter your name: ')

playerNames = player1[:11].center(11) + ' '*6 + player2[:11].center(11)

box1 = '#01'
box2 = '#02'

print('''HERE ARE 2 BOXES:
  __________       __________
 /         /|     /         /|
+---------+ |    +---------+ |
|   BOX   | |    |   BOX   | |
|   {}   | /    |   {}   | /
+---------+/     +---------+/'''.format(box1, box2))

print(playerNames)
print()
print('{}, you have a RED box in front of you.'.format(player1))
print('{}, you have a RED box in front of you.'.format(player2))
print()
print('{}, you will get to look into your box.'.format(player1))
print('{}, close your eyes and don\'t look!!!'.format(player2))
input('When  has closed their eyes, press Enter...')
print()
print('{}, here is the inside of your box'.format(player1))
isCarrot = random.choice((True, False))

if isCarrot:
        print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|      __________
 /    ||   /|     /         /|
+---------+ |    +---------+ |
|   BOX   | |    |   BOX   | |
|   {}   | /    |   {}   | /
+---------+/     +---------+/'''.format(box1, box2))
        print('There\'s carrot!')
        print(playerNames)

else:
    print('''
   _________
  |         |
  |         |
  |_________|      _________
 /         /|     /         /|
+---------+ |    +---------+ |
|   BOX   | |    |   BOX   | |
|   {}   | /    |   {}   | /
+---------+/     +---------+/'''.format(box1, box2))
    print('No carrot!')
    print(playerNames)

input('Press Enter to continue...')
print('\n'*100)

print('{}, tell {} to open their eyes.'.format(player1, player2))
input('Press Enter to continue...')
print()
print('''{}, say one of the following sentences to {}.
    1) There is carrot in my box
    2) There is no crrot in my box'''.format(player1, player2))

input('Then press Enter to continue...')

print()
while True:
    swap = input('{}, do you want to swap boxes with {} Y/N? > '.format(player1, player2)).lower()
    if swap.startswith(('y', 'n')):
        break

if swap == 'y':
    isCarrot = not isCarrot


print('''HERE ARE 2 BOXES:
  __________       __________
 /         /|     /         /|
+---------+ |    +---------+ |
|   BOX   | |    |   BOX   | |
|   {}   | /    |   {}   | /
+---------+/     +---------+/'''.format(box1, box2))

print(playerNames)
print()
input('Press Enter to reveal the winner...')

if isCarrot:
    print('''
   ___VV____        _________
  |   VV    |      |         |
  |   VV    |      |         |
  |___||____|      |_________|
 /    ||   /|     /         /|
+---------+ |    +---------+ |
|   BOX   | |    |   BOX   | |
|   {}   | /    |   {}   | /
+---------+/     +---------+/'''.format(box1, box2))
    print(playerNames)

else:
    print('''
   _________        ___VV____      
  |         |      |   VV    |
  |         |      |   VV    |
  |_________|      |___||____|
 /         /|     /    ||   /|
+---------+ |    +---------+ |
|   BOX   | |    |   BOX   | |
|   {}   | /    |   {}   | /
+---------+/     +---------+/'''.format(box1, box2))
    print(playerNames)

print('{} is the winner.'.format(player1 if isCarrot else player2))
print('Thanks for playing!')