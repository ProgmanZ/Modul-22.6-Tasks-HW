# Задача 5. Сохранение

import os


def rewrite(path, user_string):
    user_choice = 'нет'
    if os.path.exists(path):
        user_choice = input('Вы действительно хотите перезаписать файл? ').lower()
    if not os.path.exists(path) or user_choice == 'да':
        file = open(path, 'w')
        file.write(user_string)
        file.close()


def filename():
    user_file_name = input('Введите имя файла: ')
    extension = '.txt'
    if user_file_name.endswith('.txt'):
        return user_file_name
    else:
        return '{0}{1}'.format(user_file_name, extension)


def check_way(hdd_label='C:'):
    while True:
        user_ask_way = os.path.sep.join(input('Куда хотите сохранить документ? Введите '
                                              'последовательность папок (через пробел): ').split(' '))

        full_path = os.path.join(hdd_label, os.path.sep, user_ask_way)
        print(full_path)
        if os.path.exists(full_path):
            return full_path
        else:
            print('Указанного пути не существует. Повторите ввод.')


user_input = input('Введите строку: ')

user_path = check_way()
user_file = filename()
print(user_path)
print(user_file)
rewrite(os.path.join(user_path, user_file), user_input)

print('Содержимое файла', user_file)
file = open(os.path.join(user_path, user_file), 'r')
print(file.read())
file.close()
