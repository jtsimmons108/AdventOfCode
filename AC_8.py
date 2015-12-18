
lines = open('AC_8_Start.txt').read().strip().split('\n')
print lines
diff = 0
for line in lines:
    line = ''.join([letter for letter in line])
    print line, len(line), line[1:-1], len(str(line[1:-1]))
    diff += len(line) - len(str(line[1:-1]))

print diff