import string
password = [0]*8

def check_for_invalid():
    for i in range(len(password)):
        if password[i] in [8,11,14]:
            password[i] += 1
            for k in range(i + 1, len(password)):
                password[k] = 0

def increment():
    password[-1] += 1
    for i in range(len(password)-1, -1, -1):
        if password[i] == 26:
            password[i] = 0
            password[i - 1] += 1
    check_for_invalid()
            
def set_password(pw):
    for i in range(len(pw)):
        password[i] = string.lowercase.index(pw[i])
    

def has_three_straight():
    for i in range(len(password)-2):
        if password[i] + 1 == password[i+1] and password[i + 1] + 1 == password[i + 2]:
            return True
            
    return False

def has_two_pair():
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            for k in range(i+2, len(password)-1):
                if password[k] == password[k+1]:
                    if password[i] != password[k]:
                        return True
            return False
    return False
                    
def is_valid():
    return has_three_straight() and has_two_pair()                    
            
def get_password():
    return ''.join([string.lowercase[pos] for pos in password])
    

set_password('vzbxxyzz')
increment()
while(not is_valid()):
    increment()

print get_password()  
    
            
        