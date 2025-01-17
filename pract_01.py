# -*- coding: utf-8 -*-
"""Pract_01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1spm1CRe1GiZEw0VjPwBx4BP8pcQHdRGp
"""

# Задача 1

import ast

def input_list():
  user_input = input("Введите список (например, [1, 2, 3, 'hello']): ")
  try:
        # Преобразование строки в список с помощью ast.literal_eval
        user_list = ast.literal_eval(user_input)
        if isinstance(user_list, list):
            return user_list
        else:
            print("Ошибка: введенные данные не являются списком.")
            return []
  except (SyntaxError, ValueError):
        print("Ошибка: неверный формат ввода.")
        return []

# Задание 1: Индексы элементов, не являющихся числами
def find_non_numerical_indices(lst):
    non_numerical_indices = [i for i, item in enumerate(lst) if not isinstance(item, (int, float))]
    return non_numerical_indices

# Задание 2: Новый список, содержащий только числа
def filter_numbers(lst):
    numbers = [item for item in lst if isinstance(item, (int, float))]
    return numbers

example_list = input_list()
print("Ваш список:", example_list)

print("Индексы нечисловых элементов:", find_non_numerical_indices(example_list))
print("Новый список с числами:", filter_numbers(example_list))

# Задача 2

import ast

def input_list():
  user_input = input("Введите карты для игрока (6 штук) в формате [1, 2, 4, 5, 6]: ")
  try:
        user_list = ast.literal_eval(user_input)
        if isinstance(user_list, list):
            return user_list
        else:
            print("Ошибка: введенные данные не являются списком.")
            return []
  except (SyntaxError, ValueError):
        print("Ошибка: неверный формат ввода.")
        return []

player_1 = input_list();
player_2 = input_list();

score_1 = 0
score_2 = 0

for card_1, card_2 in zip(player_1, player_2):
    if card_1 > card_2:
        score_1 += card_1 + card_2
    elif card_2 > card_1:
        score_2 += card_1 + card_2

if score_1 < score_2:
    winner = "player_1"
elif score_2 < score_1:
    winner = "player_2"
else:
    winner = "Ничья"

print(f"Сумма достоинств карт у player_1: {score_1}")
print(f"Сумма достоинств карт у player_2: {score_2}")
print(f"Победитель: {winner}")

# Задача 3

input_string = input("Введите три слова через пробел: ")

words = input_string.split()

transformed_words = []
for word in words:
    transformed_word = '-'.join(word.upper())
    transformed_words.append(transformed_word)

result = ' '.join(transformed_words)

print(result)

def is_path_valid(path):
    valid_transitions = {
        'H': {'1', '2', '3', '4'}, # Коридор соединяет все комнаты
        '1': {'H'},                 # Комната 1 соединяется только с коридором
        '2': {'H'},                 # Комната 2 соединяется только с коридором
        '3': {'H'},                 # Комната 3 соединяется только с коридором
        '4': {'H'}                  # Комната 4 соединяется только с коридором
    }

    if not path:
        return False

    if path[0] != 'H' and path[-1] != 'H':
        return False

    for i in range(len(path) - 1):
        current = path[i]
        next_item = path[i + 1]

        if next_item not in valid_transitions.get(current, {}):
            return False

    return True

def get_user_path():
    while True:
        path = input("Введите путь, используя цифры 1-4 и 'H' (например, H1H2H3H4H): ")
        if all(char in '1234H' for char in path):
            return path
        else:
            print("Ошибка: путь содержит недопустимые символы. Пожалуйста, используйте только цифры 1-4 и 'H'.")

user_path = get_user_path()

if is_path_valid(user_path):
    print("Путь корректен.")
else:
    print("Путь некорректен.")