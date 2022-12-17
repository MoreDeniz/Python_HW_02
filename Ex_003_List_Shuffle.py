# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для 
# получения случайного int

def get_list():
    my_list = []
    size = int(input('Enter number: '))
    for i in range(size):
        my_list.append(random.randint(0, 99))
    return my_list

def mix_list(list_original):
    list_copy = list_original[:]
    list_length = len(list_copy)
    for i in range(list_length):
        index_mix = random.randint(0, list_length-1)
        temp = list_copy[i]
        list_copy[i] = list_copy[index_mix]
        list_copy[index_mix] = temp
    return list_copy

import random

my_list = get_list()
list_mixed = mix_list(my_list)

print(f'Original list: [', end = '')
print(*my_list, sep = ', ', end = '')
print(']')
print(f'Shuffle list:  [', end = '')
print(*list_mixed, sep = ', ', end = '')
print(']')