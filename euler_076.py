import time
from kullanislimodullerim import *
'''
It is possible to write five as a sum in exactly six different ways:
5 sayısını bir toplam olarak 6 farklı şekilde yazabiliriz:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
100 sayısını en az iki tam sayı toplamı olarak kaç farklı şekilde yazabiliriz?

logging.basicConfig(filename="076.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

'''
import copy


def diff(n,mainList=[],s=1):
    baseList = [s for i in range(n)] 
    mainList.append(baseList)
    return mainList

n = 9 
listem = []
for i in range(1,n):
    listem = diff(n,listem,s=i)

print(listem)
