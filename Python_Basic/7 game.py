import sys
import math

# Try to survive by not falling off

my_id = int(input())  # Your id, 0 or 1
height = int(input())  # height of the grid
width = int(input())  # width of the grid

# game loop
a = 0
while True:
    list = []
    for i in range(height):
        line = input()  # string describing tiles of a line of the grid containing values: 0 or 1: player with this id, '-': empty, 'x': hole
        list.append(line.split(" "))

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)    
    # print(list, file=sys.stderr, flush=True)

    Weight = [0, 0, 0, 0] # UP, RIGHT, DOWN, LEFT

    #todo

    
    # UP | RIGHT | DOWN | LEFT
    max_i = 0
    dir = ["UP", "RIGHT", "DOWN", "LEFT"]
    for i in range(1, 4):
        if Weight[i] > Weight[max_i]:
            max_i = i
    print(dir[max_i])
  
