# Задача 3. Дзен Пайтона 2

file = open('zen.txt', 'r')

count_strings = 0
count_letter = 0
count_words = 0
letters = dict()

for line in file:

    for i in line:
        if i.isalpha():
            count_letter += 1
    count_strings += 1

    for letter in set(line.lower()):
        if letter.isalpha():
            if letter not in letters:

                letters[letter] = line.count(letter)
            else:
                letters[letter] += line.count(letter)

    for word in line.strip().split():
        if not word.endswith('-'):
            count_words += 1


print('Количество букв в файле:', count_letter)
print('Количество слов в файле:', count_words)
print('Количество строк в файле:', count_strings)


period = min(letters.values())

for key, value in letters.items():
    if period == value:
        print('Наиболее редкая буква:', key)

file.close()


