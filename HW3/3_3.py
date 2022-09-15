# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 10.01] => 0.19

mas = [1.1, 1.2, 3.1, 10.01]

min = mas[0]
max = 0

for i in mas:
    fStr = str(i)
    (digit,mantisa) = fStr.split('.')
    fStr = "0." + mantisa
    ff = float(fStr)

    if min > ff or min == 0:
        min = ff

    if max < ff:
        max = ff

print(max - min)