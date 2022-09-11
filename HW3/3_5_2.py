#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#  Пример:
# для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите число: '))
negativeFirst = (-1)**(1+1)
negativeSecond = (-1)**(1+2)
positiveFirst = 0
positiveSecond = 1

result = [negativeFirst,negativeSecond,positiveFirst,positiveSecond]
K = 0
while K < k - 1:
    tmp = negativeFirst - negativeSecond
    negativeFirst = negativeSecond
    negativeSecond = tmp

    if K < k - 2:
        result.insert(0,tmp)

    tmp = positiveFirst + positiveSecond
    positiveFirst = positiveSecond
    positiveSecond = tmp
    K += 1

    result.append(tmp)

print(result)