import numpy

grid = numpy.zeros((1000,1000), dtype=numpy.int)

def turn_on(start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row + 1):
        for column in range(start_col, end_col + 1):
            grid[row][column] += 1
    

def turn_off(start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row + 1):
        for column in range(start_col, end_col + 1):
            if grid[row][column] > 0:
                grid[row][column] -= 1
    

def toggle(start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row + 1):
        for column in range(start_col, end_col + 1):
            grid[row][column] += 2
            

instruction_list = open('AC_6_Start.txt').read().split('\n')

for instruction in instruction_list:
    info = instruction.split()
    
    if 'toggle' in info:
        start_coords = info[1].split(',')
        end_coords = info[3].split(',')
        toggle(int(start_coords[0]), int(start_coords[1]), int(end_coords[0]), int(end_coords[1]))
        
    elif 'on' in info:
        start_coords = info[2].split(',')
        end_coords = info[4].split(',')
        turn_on(int(start_coords[0]), int(start_coords[1]), int(end_coords[0]), int(end_coords[1]))
    
    elif 'off' in info:
        start_coords = info[2].split(',')
        end_coords = info[4].split(',')
        turn_off(int(start_coords[0]), int(start_coords[1]), int(end_coords[0]), int(end_coords[1]))
        
lights_on = 0
for row in grid:
    lights_on += sum(row)
    
print lights_on