#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#  Пример:
# для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите число: '))
negativeFirst = (-1)**(1+1)
negativeSecond = (-1)**(1+2)

negativeFabionaci = [negativeFirst,negativeSecond]

K = 0
while K < k - 2:
    negativeFabionaci.append(negativeFabionaci[K] - negativeFabionaci[K+1])
    K += 1

positiveFabionaci = [0,1]

K = 0
while K < k - 1:
    positiveFabionaci.append(positiveFabionaci[K] + positiveFabionaci[K+1])
    K += 1


result = list()
negativeFabionaci.reverse()
result.extend(negativeFabionaci)
result.extend(positiveFabionaci)

print(result)