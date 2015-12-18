import re
sues = open('AC_16_Start.txt').read().splitlines()

sample = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
max_match = 0

for sue in sues:
    matches = 0
    info = re.split(': |, ', sue)
    for i in range(1, len(info), 2):
        if info[i] in ['cats', 'trees', 'pomeranians', 'goldfish']:
            if info[i] in ['cats', 'trees']:
                if sample[info[i]] < int(info[i+1]):
                    matches += 1
            else:
                if sample[info[i]] > int(info[i+1]):
                    matches += 1
        else:
            if sample[info[i]] == int(info[i+1]):
                matches += 1
    if matches > max_match:
        max_match = matches
        print info[0], matches