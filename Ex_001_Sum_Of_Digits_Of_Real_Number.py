# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

str = input('Enter float number: ')
res_str = str.replace('.', '')

nums = list(map(int, res_str))
sum = 0
for i in range (len(nums)):
    sum += nums[i]
print(f'Sum of digits of a real number: {str} is {sum}')