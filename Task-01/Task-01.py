# Задача 1. Сумма чисел 2.

temp = list()

file = open('numbers.txt', 'r')
new_file = open('answer.txt', 'w')

for line in file:
    temp.append(line.strip('\n').strip(' '))
file.close()

temp = sum(list(map(int, temp)))

new_file.write(str(temp))

new_file.close()

