name_of_file = input('Enter file: ')

file = open(name_of_file, 'r')
words = 0
for line in file:
    words += len(line.split(' '))
number_of_words = words


file = open(name_of_file, 'r')
number_of_lines = len(file.readlines())

print(
    f'The file contains {number_of_lines} lines and {number_of_words} words.')
