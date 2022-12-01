# Реализуйте алгоритм перемешивания списка.

import random

listFromUser = list(input('Задайте список через пробел: ').split())
print(f'Начальный список: {listFromUser}')
random.shuffle(listFromUser)
print(f'Перемешанный список: {listFromUser}')
