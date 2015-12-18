
def vowel_count(string):
    return len([letter for letter in string if letter in 'aeiou'])
    
def has_double_letter(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False
    
def has_bad_combo(string):
    bad_combos = ['ab', 'cd', 'pq', 'xy']
    for combo in bad_combos:
        if combo in string:
            return True
    return False
    
def is_nice1(string):
    return not has_bad_combo(string) and has_double_letter(string) and vowel_count(string) >= 3

def has_duplicate_letters(string):
    for i in range(len(string) - 2):
        if len(string) - len(string.replace(string[i:i+2], '', 2)) == 4:
            return True
    return False
    
def has_separated_repeat(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False

def is_nice2(string):
    return has_duplicate_letters(string) and has_separated_repeat(string)


word_list = open('AC_5_Start.txt').read().split('\n')


def challenge1():
    nice_words = 0
    for word in word_list:
        if is_nice1(word):
            nice_words += 1
    
    print nice_words
    
def challenge2():
    nice_words = 0
    for word in word_list:
        if is_nice2(word):
            nice_words += 1
    
    print nice_words
