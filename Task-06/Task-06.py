# Задача 6. Паранойя

file_input = open('text.txt', 'r')
file_output = open('cipher.txt', 'w')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz'

count = 0

for line in file_input:
    new_line = str()
    count += 1
    for letter in line:
        if letter in alphabet:
            new_line += alphabet[alphabet.index(letter)+count]
        else:
            new_line += letter
    file_output.write(new_line)


file_input.close()
file_output.close()