import sys, random, copy

EMPTY_CHAR = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
N = GRID_LENGTH ** 2

class SudokuGrid:
    def __init__(self, initialGrid):
        self.initialGrid = initialGrid

        self.grid = {}
        self.resetGrid()
        self.moves = []

    def resetGrid(self):
        self.grid = {(x, y): EMPTY_CHAR for y in range(GRID_LENGTH) for x in range(GRID_LENGTH)}

        assert len(self.initialGrid) == N
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.initialGrid[y*9 + x]
        self.updateAfterReset()
        
    def updateAfterReset(self):
        print('Reset')

    def display(self):
        print('    A B C   D E F   G H I')
        for y in range(GRID_LENGTH):
            print(y+1, end='   ')

            for x in range(GRID_LENGTH):
                print(self.grid[(x, y)], end=' ')

                if x in (2, 5):
                    print('| ', end='')
            
            print()
            if y in (2, 5):
                print('    ------+-------+------')

        print()

    def makeMove(self, col, row, num):
        x = 'ABCDEFGHI'.find(col)
        y = row - 1

        if self.grid[(x, y)] != EMPTY_CHAR:
            return False
            
        self.grid[(x, y)] = num

        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        if self.moves == []:
            return
        
        self.moves.pop()

        if self.moves == []:
            self.resetGrid()

        else:
            self.grid = copy.copy(self.moves[-1])

    def isCompleteSet(self, numbers):
        numbers = [int(n) for n in numbers]
        return sorted(numbers) == list(map(int, '123456789'))
    
    def isSolved(self):
        for y in range(GRID_LENGTH):
            rowNumbers = [self.grid[(x, y)] for x in range(GRID_LENGTH)]
            
            if '.' in rowNumbers or not self.isCompleteSet(rowNumbers):
                return False
            
        for x in range(GRID_LENGTH):
            colNumbers = [self.grid[(x, y)] for y in range(GRID_LENGTH)]

            if '.' in colNumbers or not self.isCompleteSet(colNumbers):
                return False
        
        for boxx in (0, 3, 6):
            for boxy in(0, 3, 6):
                boxNUmbers = [self.grid[(boxx + x, boxy + y)] for x in range(BOX_LENGTH) for y in range(BOX_LENGTH)]

                if '.' in boxNUmbers or not self.isCompleteSet(boxNUmbers):
                    return False

        return True

            
print('''Sudoku is a number placement logic puzzle game. A Sudoku grid is a 9x9
grid of numbers. Try to place numbers in the grid such that every row,
column, and 3x3 box has the numbers 1 through 9 once and only once.

For example, here is a starting Sudoku grid and its solved form:

    5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
    6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
    . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
    ------+-------+------     ------+-------+------
    8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
    4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
    7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
    ------+-------+------     ------+-------+------
    . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
    . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
    . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
''')

input('Press Enter to begin...')
print()

with open('sudokupuzzles.txt') as file:
    puzzles = file.readlines()

for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))


while True:
    grid.display()

    result = (grid.isSolved())
    if result:
        print('You solved the puzzle!')
        sys.exit()

    while True:
        print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:\n(For example, a move looks like "B4 9".)')

        move = input('> ').upper().strip()

        if len(move) > 0 and move[0] in ('R', 'N', 'U', 'O', 'Q'):
            break

        if len(move.split(' ')) == 2:
            (col, row), num = move.split(' ')

            if col not in list('ABCDEFGHI'):
                print('There is no column', col)
                continue
            
            if row is None or not row.isdecimal() or int(row) not in range(1, GRID_LENGTH+1):
                print('There is no row', row)
                continue

            if num is None or not num.isdecimal() or int(num) not in range(1, GRID_LENGTH+1):
                print('Select a number from 1 to 9', num)
                continue
            
            row, num = int(row), int(num)
            break    
    
    if move.startswith('R'):
        grid.resetGrid()
        continue

    if move.startswith('N'):
        grid = SudokuGrid(random.choice(puzzles))
        grid.display()

    if move.startswith('U'):
        grid.undo()
        continue

    if move.startswith('O'):
        initialGrid = SudokuGrid(grid.initialGrid)
        print('The original grid looked like this:\n')
        initialGrid.display()
        input('Press Enter to continue...\n')

    if move.startswith('Q'):
        print('Thanks for playing!')
        sys.exit()

    if grid.makeMove(col, row, num) == False:
        print('You cannot overwrite a grid\'s numbers.')
        print('Enter ORIGINAL to view the original grid.')
        input('Press Enter to continue...')