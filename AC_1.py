
text = open('AC_1_Start.txt').read()
moves = {'(':1, ')':-1}


'''
Advent of Code
Day 1 Challenge 1
Determine Santa's Floor level
'''
def challenge1():
    print sum([moves[char] for char in text if char in moves.keys()])
    

'''
Advent of Code
Day 1 Challenge 1
Determine Santa's First Step Into Basement
'''
def challenge2():
    sum_ = 0
    position = 0
    for char in text:
        if char in moves.keys():
            sum_ += moves[char]
            position += 1
            if sum_ < 0:
                print position
                break

