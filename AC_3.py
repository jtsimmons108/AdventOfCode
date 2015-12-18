import PIL
import matplotlib.pyplot as plt
import numpy as np
directions = open('AC_3_Start.txt').read()

'''
Advent of Code
Day 3 Challenge 1
Determine Santas Houses
'''


def challenge1():
    curr_x = 0
    curr_y = 0
    houses = {(0,0):1}
    for direction in directions:
        if direction == '>':
            curr_x += 1
        elif direction == '<':
            curr_x -= 1
        elif direction == '^':
            curr_y += 1
        elif direction == 'v':
            curr_y -= 1
        if (curr_x, curr_y) not in houses.keys():
            houses.update({(curr_x, curr_y):1})
        else:
            houses[(curr_x, curr_y)] += 1
    '''img = PIL.Image.new('RGB', (100,100))
    image = np.array(img)
    for key in houses.keys():
        print key[0], key[1]
        image[50 + key[0]][50 + key[0]] = [255,0,0]
    fig, ax = plt.subplots(1,1)
    ax.imshow(image)
    fig.show()'''
    print len(houses)

'''
Advent of Code
Day 1 Challenge 1
Determine Santa's First Step Into Basement
'''

def challenge2():
    curr_positions = [[0,0],[0,0]]
    
    houses = {(0,0):2}
    for index in range(len(directions)):
        if directions[index] == '>':
            curr_positions[index % 2][0] += 1
        elif directions[index] == '<':
            curr_positions[index % 2][0] -= 1
        elif directions[index] == '^':
            curr_positions[index % 2][1] += 1
        elif directions[index] == 'v':
            curr_positions[index % 2][1] -= 1
        
        curr_x = curr_positions[index % 2][0]
        curr_y = curr_positions[index % 2][1]
        if (curr_x, curr_y) not in houses.keys():
            houses.update({(curr_x, curr_y):1})
        else:
            houses[(curr_x, curr_y)] += 1
    print houses
    print len(houses)

