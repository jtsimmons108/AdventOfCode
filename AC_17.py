from itertools import combinations

containers = sorted([int(val) for val in open('AC_17_Start.txt').read().strip().split('\n')])
print [len([combo for combo in combinations(containers, i) if sum(combo) == 150]) for i in range(3,9)]