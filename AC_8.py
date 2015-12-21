
lines = open('AC_8_Start.txt').read().strip().split('\n')
diff = 0
for line in lines:
    print line
    total = 0
    for letter in line:
        if letter in '\\"':
            total += 2
        else:
            total += 1
    diff += total - len(line) + 2

print diff