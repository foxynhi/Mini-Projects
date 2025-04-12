import random, sys

BLANK = ' '

def main():
    print('You win if you can create a 2048 tile. \nYou lose if the board fills up the tiles before then.')

    input('\nPress Enter to play...')
    score = 0
    board = createBoard()
    while True:
        displayBoard(board)

        print('Score:', getScore(board, score))
        
        move = getMove()

        board = (makeMove(board, move))
        
        while True:
            randomTwo = random.randint(0, 3), random.randint(0, 3)
            if board[randomTwo] == BLANK:
                board[randomTwo] = 2
                break
    
        if isFull(board) == True:
            print('Game over!')
            sys.exit()

def createBoard():
    newBoard = {(x, y): BLANK for x in range(4) for y in range(4)}
    
    firstTwos = 0

    while firstTwos < 6:
        place = random.randint(0, 3), random.randint(0, 3)

        if newBoard[place] == BLANK:
            newBoard[place] = 2
            firstTwos += 1
    return newBoard

def displayBoard(board):
    value = [str(board[(x, y)]).center(5) for y in range(4) for x in range(4)]
    
    print('''
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+'''.format(*value))
    
def getScore(board, score):
    sum = 0
    for x in range(4):
        for y in range(4):
            temp = board[(x, y)]
            if type(temp) == int:
                sum += temp
    return score + sum

def getMove():
    while True:
        print('Enter move: (WASD or Q to quit)')
        move = input('> ')

        if move.upper() in ('W', 'A', 'S', 'D', 'Q'):
            return move.upper()

def makeMove(board, move):
    allSpaces = []
    if move == 'A':
        allSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                     [(0, 1), (1, 1), (2, 1), (3, 1)],
                     [(0, 2), (1, 2), (2, 2), (3, 2)],
                     [(0, 3), (1, 3), (2, 3), (3, 3)]]
        
    elif move == 'W':
        allSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                     [(1, 0), (1, 1), (1, 2), (1, 3)],
                     [(2, 0), (2, 1), (2, 2), (2, 3)],
                     [(3, 0), (3, 1), (3, 2), (3, 3)]]
    
    elif move == 'S':
        allSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                     [(1, 3), (1, 2), (1, 1), (1, 0)],
                     [(2, 3), (2, 2), (2, 1), (2, 0)],
                     [(3, 3), (3, 2), (3, 1), (3, 0)]]
        
    elif move == 'D':
        allSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                     [(3, 1), (2, 1), (1, 1), (0, 1)],
                     [(3, 2), (2, 2), (1, 2), (0, 2)],
                     [(3, 3), (2, 3), (1, 3), (0, 3)]]

    else:
        sys.exit()
        
    boardAfterMove = {}
    for colSpaces in allSpaces:
        firTileSpace = colSpaces[0]
        secTileSpace = colSpaces[1]
        thiTileSpace = colSpaces[2]
        fouTileSpace = colSpaces[3]

        firTile = board[firTileSpace]
        secTile = board[secTileSpace]
        thiTile = board[thiTileSpace]
        fouTile = board[fouTileSpace]
        
        column = [firTile, secTile, thiTile, fouTile]
        
        combinedCol = combineTiles(column)

        boardAfterMove[firTileSpace] = combinedCol[0]
        boardAfterMove[secTileSpace] = combinedCol[1]
        boardAfterMove[thiTileSpace] = combinedCol[2]
        boardAfterMove[fouTileSpace] = combinedCol[3]
    
    return boardAfterMove

def combineTiles(column):
    combinedColumn = []

    for i in range(4):
        if type(column[i]) == int:
            combinedColumn.append(column[i])

    lenOfCombinedColumn = len(combinedColumn)
    if lenOfCombinedColumn < 5:
        combinedColumn += [BLANK] * (4 - lenOfCombinedColumn)

    for i in range(3):
        if combinedColumn[i] == combinedColumn[i+1]:
            combinedColumn[i] *= 2

            for j in range(i+1, 3):
                combinedColumn[j] = combinedColumn[j+1]
            combinedColumn[3] = BLANK

    return combinedColumn

def isFull(board):
    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False
            
    return True

if __name__ == '__main__':
    main()