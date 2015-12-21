import itertools
seating_prefs = open('AC_13_Start.txt').read().strip().split('\n')
pref_nums = {}
people = set()
for line in seating_prefs:
    info = line[0:-1].split()
    people |= set([info[0]])
    if info[2] == 'gain':
        pref = int(info[3])
    else:
        pref = -int(info[3])
    pref_nums.update({(info[0], info[-1]):pref})
for person in people:
    pref_nums.update({(person, 'me'):0})
    pref_nums.update({('me', person):0})

people |= set(['me'])
all_vals = []   
'''combo = list(('David', 'Eric', 'Carol', 'Frank', 'Bob', 'Alice', 'Mallory', 'George'))
print combo
for i in range(9):
    new_combo = combo[::]
    new_combo.insert(i, 'me')
    print new_combo
    vals = []
    for i in range(len(new_combo)-1):
        vals += [pref_nums[(new_combo[i], new_combo[i-1])]]
        vals += [pref_nums[(new_combo[i], new_combo[i + 1])]]
    vals += [pref_nums[(new_combo[-1], new_combo[0])]]
    vals += [pref_nums[(new_combo[-1], new_combo[-2])]]
    all_vals += [sum(vals)]
    
    print new_combo, sum(vals)'''
    
for combo in itertools.permutations(people):
    vals = []
    for i in range(len(combo)-1):
        vals += [pref_nums[(combo[i], combo[i-1])]]
        vals += [pref_nums[(combo[i], combo[i + 1])]]
    vals += [pref_nums[(combo[-1], combo[0])]]
    vals += [pref_nums[(combo[-1], combo[-2])]]
    all_vals += [sum(vals)]
  
    
print max(all_vals)
        