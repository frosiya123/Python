# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):

# С помощью использования **лямбд, filter, map, zip, enumerate,
# list comprehension


# 1. Напишите программу, которая будет преобразовывать десятичное число
#  в двоичное (без встроенных функций).
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10



# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
#- [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12
# задача решается с использованием метода reduce

arr = [2, 3, 5, 9, 3]
from functools import reduce
# mylist = [arr[i] for i in range(1, len(arr),2)]
result = reduce(
    (lambda x,y: x+y), 
    [arr[i] for i in range(1, len(arr),2)]
)

print(result)