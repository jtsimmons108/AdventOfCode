import time
paper_amounts = open('AC_2_Start.txt').read().strip().split('\n')

dimension_list = []
for amount in paper_amounts:
        dimension_list.append(sorted([int(dim) for dim in amount.split('x')]))

'''
Advent of Code
Day 2 Challenge 1
Determine Wrapping Paper Amount
'''
def challenge1():
    total_paper = 0
    for dimension in dimension_list:
        total_paper += 3*dimension[0]*dimension[1] + 2 * dimension[0]*dimension[2] + 2*dimension[1]*dimension[2]
    print total_paper
    

'''
Advent of Code
Day 1 Challenge 1
Determine Santa's First Step Into Basement
'''
def challenge2():
    total_ribbon = 0
    for dimension in dimension_list:
        total_ribbon += 2*(dimension[0] + dimension[1]) + dimension[0]*dimension[1]*dimension[2]
    print total_ribbon

start = time.time()
challenge1()
print time.time() - start

