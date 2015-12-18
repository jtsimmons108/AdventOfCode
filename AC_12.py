import json

string = open('AC_12_Start.txt').read()
i = 0
total = 0
'''while i < len(string):
    if string[i] in '-0123456789':
        length = 1
        while string[i + length] in '0123456789':
            length += 1
        total += int(string[i:i+length])
        i += length
        
    i += 1
    
print total'''

for element in json.loads(string):
    for inner in element:
        for more_inner in inner:
            print more_inner