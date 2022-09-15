# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

num_1 = int(input('Введите натуральное число: '))
list_1 = []
simple = 2
while num_1 > 1:
    if num_1 % simple == 0:
        list_1.append(simple)
        num_1 = num_1 / simple
    else:
        simple += 1

print(list_1)
