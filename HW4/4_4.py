# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов  (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:

#     k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень числа: '))

sstr = ''
while k > 0:
    sstr += str(random.randint(0,100)) + 'x' + '^' + str(k) + ' + '
    k -= 1

sstr += str(random.randint(0,100)) + ' = 0'

#print(sstr)
data = open('fail1.txt', 'w')
data.writelines(sstr)
data.close