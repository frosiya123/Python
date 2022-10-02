# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):

# С помощью использования **лямбд, filter, map, zip, enumerate,
# list comprehension


# Задайте список из k чисел последовательности (1 + 1\k)^k 
# и выведите на экран их сумму.

# k = int(input('Введите число к: '))
# from functools import reduce
# k = 3

# ksum = 0
# ksum = reduce(
#      (lambda x,y: x+y), 
#     list(map(lambda x: (1 + 1/ x)**x, range(1,k+1)))
# )

# print(ksum)



# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
#- [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12
# задача решается с использованием метода reduce

# arr = [2, 3, 5, 9, 3]
# from functools import reduce
# # mylist = [arr[i] for i in range(1, len(arr),2)]
# result = reduce(
#     (lambda x,y: x+y), 
#     [arr[i] for i in range(1, len(arr),2)]
# )

# print(result)



from functools import reduce

arr = [1,2,3,4,5,6,7]
elementSum = reduce(
    lambda x,y: x+y, 
    filter(lambda index: ((index -1) %2 != 0), range(1,len(arr)+1))
)
print(elementSum)
#