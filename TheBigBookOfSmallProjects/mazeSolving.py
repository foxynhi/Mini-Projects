MAZE = """#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################""".split('\n')

HEIGHT = len(MAZE)
WIDTH = len(MAZE[1])
EMPTY = ' '
PATH = '.'
START = 'S'
EXIT = 'E'


for line in range(HEIGHT):
    MAZE[line] = list(MAZE[line])

def printMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(maze[y][x], end='')
        print()
    print()

def mazeSolving(maze, x=1, y=1, visited=None):
    if maze[y][x] == EXIT:
        return True
    if visited == None:
        visited = []
    if maze[y][x] != START:
        maze[y][x] = PATH
    visited.append(str(x) + ',' + str(y))

    if x + 1 < WIDTH and maze[y][x+1] in [EMPTY, EXIT] and (str(x+1) + ',' + str(y)) not in visited:
        if mazeSolving(maze, x+1, y, visited):
            return True
        
    if x - 1 >= 0 and maze[y][x-1] in [EMPTY, EXIT] and (str(x-1) + ',' + str(y)) not in visited:
        if mazeSolving(maze, x-1, y, visited):
            return True
    
    if y + 1 < HEIGHT and maze[y+1][x] in [EMPTY, EXIT] and (str(x) + ',' + str(y+1)) not in visited:
        if mazeSolving(maze, x, y+1, visited):
            return True
        
    if y - 1 >= 0  and maze[y-1][x] in [EMPTY, EXIT] and (str(x) + ',' + str(y-1)) not in visited:
        if mazeSolving(maze, x, y-1, visited):
            return True
        
    maze[y][x] = EMPTY
    printMaze(maze)
    return False

mazeSolving(MAZE)
printMaze(MAZE)