# Задача 8. Частотный анализ


def calculate(count_frequency, input_string):
    len_words = len([letter for letter in input_string if letter.isalpha()])
    return (count_frequency / len_words) / 10


user_file = open('text.txt', 'r')
user_string = user_file.read().lower()
user_file.close()

# Создание словаря с ключами-буквами и значениями в виде подсчета частоты буквы
user_db = {letter: calculate(user_string.count(letter), user_string) for letter in set(user_string) if letter.isalpha()}

# Создание нового словаря с ключами-значениями частоты и пустыми списками в которые будут загружены буквы с такой же
# частотой
reverse_db = {key: list() for key in set(user_db.values())}

# for r_key in reverse_db.keys():
#     for key, value in user_db.items():
#         if r_key == value:
#             reverse_db[r_key] += key

# Наполнение значениями-буквами созданного ранее словаря
[reverse_db[r_key].append(key) for key, value in user_db.items() for r_key in reverse_db.keys() if r_key == value]


# for key in sorted(reverse_db.keys(), reverse=True):
#     for value in sorted(reverse_db[key]):
#         print(f'{value} {key}')
#

# Вывод словаря согласно условию задачи
output_file = open('analysis.txt', 'w')

[output_file.write(f'{value} {key:.4f}\n')
 for key in sorted(reverse_db.keys(), reverse=True)
 for value in sorted(reverse_db[key])]

output_file.close()

