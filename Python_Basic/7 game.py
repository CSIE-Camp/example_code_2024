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

    print(list, file=sys.stderr, flush=True)
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    
    # UP | RIGHT | DOWN | LEFT