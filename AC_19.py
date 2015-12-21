
word_file = open('AC_19_Start_Word.txt')
start_word = word_file.read().strip()
word_file.close()

command_file = open('AC_19_Commands.txt')
command_list = command_file.read().strip().split('\n')
command_file.close()
combos = set()
length = len(start_word)
for command in command_list:
    info = command.split()
    target = info[0]
    replace = info[2]
    current = 0
    for times in range(start_word.count(target)):