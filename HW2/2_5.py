#Реализуйте алгоритм перемешивания списка.

from random import random
import random

arr = [1,2,3,4,5,6,7,8,9,10]
ellementsCount = len(arr)

for i in arr:
    startEll = random.randint(0,ellementsCount-1)
    endEll = random.randint(0,ellementsCount-1)

    tmp = arr[startEll]
    arr[startEll] = arr[endEll]
    arr[endEll] = tmp

print(arr)