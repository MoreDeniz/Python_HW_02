# Задайте список из n чисел последовательности (1 + 1/n)^n, 
# выведеите его на экран, а также сумму элементов списка.
# Пример:
# Для n = 4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Enter natural number: '))
list_num = []
sum = 0
for i in range (1, n + 1):
    res = round((1 + 1/i) ** i, 2)
    list_num.append(res)
    sum += res
print(f'For n = {n} --> [', end = '')
print(*list_num, sep = ', ', end = '')
print(']')
print(f'Sum = {sum}.')
