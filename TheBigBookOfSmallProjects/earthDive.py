import sys, random, time

WIDTH = 70
GAPWIDTH = 10
char = '#'

print('Press Ctrl+C to stop')
time.sleep(2)

leftWidth = 20

while True:
    temp = random.randint(1, 6)
    if temp == 1 and (leftWidth + GAPWIDTH < WIDTH - 1):
        leftWidth += 1
    elif temp == 2 and leftWidth > 1:
        leftWidth -= 1

    print(char * leftWidth + ' ' * GAPWIDTH + char * (WIDTH - GAPWIDTH - leftWidth))

    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()
