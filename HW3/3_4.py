# Напишите программу, которая будет преобразовывать десятичное число
#  в двоичное (без встроенных функций).
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

number = 45
binstr = ''

while number > 0:
    binstr = str(number % 2) + binstr
    number = int(number/2)

print(binstr)