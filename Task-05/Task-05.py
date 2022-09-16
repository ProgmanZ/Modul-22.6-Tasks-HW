# Задача 5. Сохранение

import os


def rewrite(path):
    if os.path.exists(path):
        while True:
            user_choice = input('Вы действительно хотите перезаписать файл? ').lower()
            if user_choice == 'да':
                return True
            elif user_choice == 'нет':
                return False
            else:
                print('Ответ не совпадает. Возможны 2 варианта ответа: \'да\' и \'нет\'.')
                continue
    else:
        return False


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
if rewrite(os.path.join(user_path, user_file)):
    file = open(os.path.join(user_path,user_file), 'w')
    file.write(user_input)
    file.close()

print('Содержимое файла', user_file)
file = open(os.path.join(user_path, os.path.sep, user_file), 'r')
print(file.read())
file.close()
