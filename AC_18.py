import numpy

grid = numpy.zeros((100,100), dtype = numpy.int)
grid_text = open('AC_18_Start.txt').read().strip().split('\n')
for row in range(len(grid_text)):
    for column in range(len(grid_text[0])):
        if grid_text[row][column] == '#':
            grid[row][column] = 1
        else:
            grid[row][column] = 0



def is_valid(row, column):
    return row >=0 and row <= 99 and column >= 0 and column <=99

def neighbor_sum(row, column):
    total = 0
    for deltar in range(-1,2):
        for deltac in range(-1, 2):
            if is_valid(row + deltar, column + deltac):
                total += grid[row + deltar][column + deltac]
                
    total -= grid[row][column]
    return total

for i in range(100):
    temp_grid = numpy.zeros((100,100), dtype = numpy.int)
    for row in range(100):
        for column in range(100):
            if (row, column) in [(0,0), (0,99), (99,0), (99,99)]:
                temp_grid[row][column] = 1
            else:
                neighbors = neighbor_sum(row,column)
                if grid[row][column] == 1:
                    if neighbors == 2 or neighbors == 3:
                        temp_grid[row][column] = 1
                    else:
                        temp_grid[row][column] = 0
                else:
                    if neighbors == 3:
                        temp_grid[row][column] = 1
                    else:
                        temp_grid[row][column] = 0
    grid = temp_grid

total = 0
for row in grid:
    total += sum(row)
print total
    

    
