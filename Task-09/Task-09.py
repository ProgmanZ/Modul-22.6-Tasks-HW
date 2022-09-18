# Задача 9. Война и мир (необязательная)

import zipfile


# Функция подсчета частоты буквы в тексте в процентах от всего текста
def calculate(count_frequency, input_string):
    len_text = len([letter for letter in input_string if letter.isalpha()])
    return (count_frequency / len_text) * 100


# Распаковка файла "voina-i-mir.zip"
zip_file = zipfile.ZipFile('voina-i-mir.zip', 'r')
zip_file.extractall('')
zip_file.close()

# Открытие распакованного файла "voina-i-mir.txt"
input_file = open('voina-i-mir.txt', 'r', encoding='utf-8')
all_text = input_file.read()
input_file.close()

# Создание словаря с ключами-буквами и значениями в виде подсчета частоты буквы
user_db = {letter: calculate(all_text.count(letter), all_text) for letter in set(all_text) if letter.isalpha()}

# Создание нового словаря с ключами-значениями частоты и пустыми списками в которые будут загружены буквы с такой же
# частотой
reverse_db = {key: list() for key in set(user_db.values())}

# Наполнение значениями-буквами созданного ранее словаря
[reverse_db[r_key].append(key) for key, value in user_db.items() for r_key in reverse_db.keys() if r_key == value]

# Вывод словаря на экран по убыванию частоты
[print(f'Буква "{value}" составляет {key:.4f}% от всего текста') for key in sorted(reverse_db.keys(), reverse=True)
    for value in sorted(reverse_db[key])]

