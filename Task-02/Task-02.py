# Задача 2. Дзен Пайтона

file = open('zen.txt', 'r')
text = file.read().split('\n')
file.close()

text = text[::-1]
for line in text:
    print(line)
