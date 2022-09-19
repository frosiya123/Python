# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все
#  конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# для выигрыша первого игрока надо отсчитать конфеты по формуле
#остаток = (2021/ (28+1)). И для каждого хода брать остаток от деления

# игрок 1 должен все время вводить число посчитанное по формуле
# игрок 2 модет вводить число рандомно
import random

allsum = 196
divider = 28
#remander1 = (allsum % (divider+1))

firstPlayer = []
secondPlayer = []

while allsum > 0:
    # Ход первого игрока
    firstPlayerStep = allsum % (divider+1)

    if allsum < 29:
        firstPlayer.append(allsum)
        break

    if firstPlayerStep == 0:    
        firstPlayerStep = 28

    firstPlayer.append(firstPlayerStep)
    allsum -= firstPlayerStep
    
    # Ход вторго игрока
    secondPlayerStep = random.randint(0,29)

    secondPlayer.append(secondPlayerStep)
    allsum -= secondPlayerStep

print(firstPlayer)
print(secondPlayer)
   