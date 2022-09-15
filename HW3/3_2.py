#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй 
# и предпоследний и т.д.
# Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

mas = [2, 3, 5, 6]
destArr = list()

size = len(mas)
diff = size % 2
middle = int(size / 2)

i = 0
j = size - 1

while i < middle + diff:
    destArr.append(mas[i] * mas[j-i])
    i += 1

print(destArr)
