#Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N].
#Найдите произведение элементов на указанных 
# пользователем через пробел позициях. 

num = int(input('Введите число N: '))
position = input('Введите позиции через пробел: ')
positions = position.split(' ')

arr = list(range(-num,num+1))

print(arr)
digitMultiplication = 1
check = 1
for i in positions:
    i = int(i) - 1
    if i < 0 or i > num:
        print("Такой позиции как ", i+1, " не существует")
        check = 0
        break

    if arr[i] or arr[i] == 0:
        digitMultiplication *= arr[i]

if check:
    print(digitMultiplication)