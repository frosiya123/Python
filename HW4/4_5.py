# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Результат вычислений
resultDict = {}

def readFile(fileName):
    sstr1 = '/home/mamus/Моя учеба/git/Python/fail1.txt'
    f = open(fileName, 'r')
    data = f.read() + ' '
    f.close()
    data = data.replace(' ', '')
    data = data.replace('=0', '')

    multMembers = data.split('+')

    for i in multMembers:
        #print(i)
        members = i.split("x^",2)
        if len(members) > 1:
            if members[1] in resultDict:
                resultDict[str(members[1])] += int(members[0])
            else:
                resultDict[str(members[1])] = int(members[0])
        else:
            if "0" in resultDict:
                resultDict["0"] += int(members[0])
            else:
                resultDict["0"] = int(members[0])

    return "Success"

files = [
    '/home/mamus/Моя учеба/git/Python/fail1.txt',
    '/home/mamus/Моя учеба/git/Python/fail12.txt'
]

f = open('/home/mamus/Моя учеба/git/Python/fail13.txt', 'w')

for i in files:
    readFile(i)

lstr = ''
for i in sorted(resultDict.keys(),reverse=True):
    if i != "0":
        lstr += str(resultDict[i]) + 'x^' + str(i) + ' + '
    else:
        lstr += str(resultDict["0"]) + ' = 0'

f.write(lstr)
f.close()

