# Задача 7. Турнир

input_file = open('first_tour.txt', 'r')


max_number = int(input_file.readline()) # Чтение лимита из файла
list_name = list()  # Список для проверки имен во время записи результатов
text = dict() # Скорректированная база {('P', 'Segeev'): 92, ('V', 'Petrov'): 98, ('M', 'Vasiliev'): 98}
count = 0 # Счетчик для записи номера участника и для записи количества в первую строку

for line in input_file:
    line = line.strip().split()
    if int(line[-1]) > max_number:
        count += 1
        text[line[1][0], line[0]] = int(line[-1])

result_list = sorted(text.values(), reverse=True)

output_file = open('second_tour.txt', 'a')
output_file.write(str(count))

count = 0

for val in sorted(text.values(), reverse=True):
    for key, value in text.items():
        if value == val and key not in list_name:
            count += 1
            output_file.write(' '.join(['\n' + str(count) + ')', '.'.join(key), str(val)]))
            list_name.append(key)

input_file.close()
output_file.close()
