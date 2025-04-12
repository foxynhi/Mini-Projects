import random, copy, time, sys

HEIGHT = 20
WIDTH = 70

ALIVE = 'o'
DEAD = ' '
nextCells = {}

for x in range(WIDTH):
    for y in range(HEIGHT):
        temp = random.randint(0, 1)
        nextCells[(x, y)] = ALIVE if temp == 1 else DEAD

while True:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(nextCells[(x, y)], end='')
        print()

    print('Quit anytime!\n')
    print('\n'*5)
    cells = copy.deepcopy(nextCells)
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = 0
            left = x-1 if x-1 >= 0 else None
            right = x+1 if x+1 < WIDTH else None
            above = y-1 if y-1 >= 0 else None
            below = y+1 if y+1 < HEIGHT else None
            
            try: 
                if cells[(left, y)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(left, above)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(x, above)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(right, above)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(right, y)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(right, below)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(x, below)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass
            try: 
                if cells[(left, below)] == ALIVE:
                    neighbors += 1
            except KeyError:
                pass

            if cells[(x, y)] == ALIVE and neighbors in (2, 3):
                nextCells[(x, y)] == ALIVE
            elif cells[(x, y)] == DEAD and neighbors == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD
    
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('Thanks!')
        sys.exit()