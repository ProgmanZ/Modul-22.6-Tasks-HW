# Задача 4. Файлы и папки

import os


def check_input(user_input=False):

    while not user_input:
        entered = input()
        user_input = os.path.exists(entered)
        if not user_input:
            print('Введен несуществующий путь. Попробуйте еще раз.')
            continue
        return entered


def settings(object_path, count_size=0, count_dir=0, count_file=0):

    for item in os.listdir(object_path):

        i_path = os.path.join(os.path.abspath(object_path), item)

        if os.path.isfile(i_path):
            count_file += 1
            count_size += os.path.getsize(i_path)

        if os.path.isdir(i_path):
            count_dir += 1
            count_size, count_dir, count_file = settings(i_path, count_size, count_dir, count_file)

    return count_size, count_dir, count_file


all_size, quantity_dirs, quantity_files = settings(check_input())

print('Размер каталога (в Кб): {0}\n'
      'Количество подкаталогов: {1}\n'
      'Количество файлов: {2}'.format(all_size/1000, quantity_dirs, quantity_files))
