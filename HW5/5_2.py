#Создайте программу для игры в ""Крестики-нолики"".
# игра с ботом
import random

xoField = {}
filds = [[None,None,None], [None,None,None], [None,None,None]]


def botStep():
    row = random.randint(0,2)
    col = random.randint(0,2)

    if filds[row][col]:
        return None

    filds[row][col] = 'O'

    print("Бот походил: " + str(row) + ' ' + str(col))
    return {"row": row, "col": col}

# Функция, которая возвращает, где находятся X и 0
def checkPostions(sDirection,simbolXO,positionXO):
    if sDirection == 'dia':
        i = 0
        j = 0
        countSuccess = 0
        for i in range(0,3):
            if filds[i][j] != simbolXO:
                break
            i += 1
            j += 1
            countSuccess += 1
        
        if countSuccess == 3:
            return 'Victory'

        i = 2
        j = 0
        for j in range(0,3):
            if filds[i][j] != simbolXO:
                return None
            i -= 1
            j += 1
        return 'Victory'

    countSuccess = 0
    for getPostion in xoField[simbolXO]:
        if getPostion[sDirection] == positionXO[sDirection]:
            countSuccess +=1

    if countSuccess == 2:
        return 'Victory'

    return None

# функция признак победы
def victoryValidate(simbolXO, positionXO):
    # проверка столбцаБ строки и диагонали на свопадение символов
    if not xoField[simbolXO] or len(xoField[simbolXO]) < 2:
        xoField[simbolXO].append(positionXO)
        return None
    
    for prevRow in xoField[simbolXO]:
        i = prevRow["col"] - positionXO["row"]
        j = prevRow["row"] - positionXO["row"]

        if i == 0:
            # Проверка по строке
            if checkPostions('row',simbolXO,positionXO):
                return 'Victory'
            
        if j == 0:
            # Проверка по колонке
            if checkPostions('col',simbolXO,positionXO):
                return 'Victory'

       
        if checkPostions('dia',simbolXO,positionXO):
            return 'Victory'
    
    xoField[simbolXO].append(positionXO)

allFilds = 0
xoField['X'] = []
xoField['O'] = []

while allFilds != 9:
    d = input("Введите координаты точки X через пробел ")

    [i,j] = d.split(' ')
    row = int(i)
    col = int(j)

    if row > 2 or col > 2:
        print("Введены не верные координаты")
        continue

    if filds[row][col]:
        print("В этой точек уже стоит " + filds[row][col])
        continue

    filds[row][col] = 'X'
    if victoryValidate('X',{"row": row, "col": col}):
        print("Победил Х за " + str(allFilds+1) + " хода")
        exit()

    while True:
        positionO = botStep()
        if  positionO:
            if victoryValidate('O',{"row": positionO["row"], "col": positionO["col"]}):
                print("Победил O за " + str(allFilds+1) + " хода")
                exit
            break

    print(filds)
    allFilds += 1

    