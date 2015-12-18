
def look_and_say(string):
    if len(string) == 1:
        return '1' + string
    else:
        index = 0
        count = 1
        result = ''
        while index < len(string) - 1:
            if string[index] == string[index + 1]:
                count += 1
            else:
                result += str(count) + string[index]
                count = 1   
                
            index += 1
        
        if string[-2] == string[-1]:
            result += str(count) + string[-1]
        else:
            result += '1' + string[-1]
        return result
        
start = '1113122113'
for i in range(50):
    start = look_and_say(start)

print len(start)