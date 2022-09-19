# Реализуйте RLE алгоритм: реализуйте модуль сжатия и 
# восстановления данных.(пробелы тоже считает)
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def rleEnCode(data):
    enCode = ''
    prewChair = ''
    count = 1
    if not data:
        return ''

    for chair in data:
        if chair != prewChair:
            if prewChair:
                enCode += str(count) + prewChair
            count = 1
            prewChair = chair
        else:
            count += 1
    else:
        enCode +=  str(count) + prewChair
        return(enCode)

with open('/home/mamus/Моя учеба/git/Python/fail22.txt', 'r') as data:
    rleEnCode1 = data.readline()
#print(rleEnCode1)
rleEnCode1 = str(rleEnCode1.split(' '))
#print(rleEnCode1)
enCodeVal = rleEnCode(rleEnCode1)
print(enCodeVal)


def rleDecoder(data1):
    decode = ''
    count1 = ''
    for chair in data1:
        if chair.isdigit():
            count1 += chair
        else:
            decode += chair * int(count1)
            count1 = ''
    return decode

decodedVal = rleDecoder(enCodeVal)
#print(decodedVal)
data3 = open('fail23.txt', 'w')
data3.writelines(decodedVal)
data3.close


