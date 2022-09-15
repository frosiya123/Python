# Вычислить число c заданной точностью d
# Пример:

#     при $d = 0.001, π = 3.141
import math

d = input('Введите d: ')
pi = math.pi
pistr = str(pi)

def afterPoint(fDigit):
    getStr = str(fDigit)
    out = getStr.split('.')
    return len(out[1])

out = pistr.split('.')
print(out[0]+'.'+out[1][0:afterPoint(d)])

