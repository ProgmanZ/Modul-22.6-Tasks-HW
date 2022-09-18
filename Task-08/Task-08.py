# Задача 8. Частотный анализ


user_string = 'Mama myla ramu'.lower()


def calculate(count_frequency, input_string):
    len_words = len([letter for letter in input_string if letter.isalpha()])
    return (count_frequency / len_words) / 10


user_db = {letter: calculate(user_string.count(letter),user_string) for letter in set(user_string) if letter.isalpha()}

reverse_db = {key: list() for key in set(user_db.values())}

# for r_key in reverse_db.keys():
#     for key, value in user_db.items():
#         if r_key == value:
#             reverse_db[r_key] += key

[reverse_db[r_key].append(key) for key, value in user_db.items() for r_key in reverse_db.keys() if r_key == value]


# for key in sorted(reverse_db.keys(), reverse=True):
#     for value in sorted(reverse_db[key]):
#         print(f'{value} {key}')
#

[print(f'{value} {key:.4f}') for key in sorted(reverse_db.keys(), reverse=True) for value in sorted(reverse_db[key])]

