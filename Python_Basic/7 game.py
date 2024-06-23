import sys
import math

# Try to survive by not falling off

my_id = int(input())  # Your id, 0 or 1
height = int(input())  # height of the grid
width = int(input())  # width of the grid

# game loop

while True:
    list = []
    for i in range(height):
        line = input()  # string describing tiles of a line of the grid containing values: 0 or 1: player with this id, '-': empty, 'x': hole
        list.append(line.split(" "))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)    
    # print(list, file=sys.stderr, flush=True)

    Weight = [0, 0, 0, 0] # UP, RIGHT, DOWN, LEFT

    '''
    Hint:
    1. 當你覺得往上走比較好時，Weight[0] += 1(或更大的值)(其他方向以此類推)
    2. 當你覺得往上走比較不好時，Weight[0] -= 1(或更小的值)(其他方向以此類推)
    3. 盡可能想更多的情況，以達到更好的結果
    4. 加油！這堂課即將進入尾聲，希望你能學到東西！
    '''

    # TODO

    
    # UP | RIGHT | DOWN | LEFT
    max_i = 0
    dir = ["UP", "RIGHT", "DOWN", "LEFT"]
    for i in range(1, 4):
        if Weight[i] > Weight[max_i]:
            max_i = i
    print(dir[max_i])
  
