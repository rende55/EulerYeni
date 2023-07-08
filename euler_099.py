# PROBLEM NO.99
'''
Comparing two numbers written in index form like 211 and 37 is not difficult, 
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), 
a 22K text file containing one thousand lines with a base/exponent pair on each line, 
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import time
import copy
import logging
from itertools import *

with open("p099_base_exp.txt", 'r') as liste1:     #listemizi dosyadan çekiyoruz.
    lines = liste1.read().splitlines()


listeTum = list()
for eleman in lines:
    eleman = eleman.split(',')
    listeTum.append(eleman)

for satir in listeTum:
    for indis, deger in enumerate(satir):
        satir[indis] = int(deger)

# ------------------------------------------------------------------------------------------------


minus = 10**10
listemX = copy.deepcopy(listeTum)
for list in listemX:
    if list[1]<minus:
        minus = list[1]
print(f'en düşük üs = {minus}')
for list in listemX:
    list[1] = list[1]/minus

maksDeger = 1
for indis,liste in enumerate(listemX):
    value = liste[0]**liste[1]
    if  value> maksDeger:
        sira = indis
        maksDeger = value
print(f'maksimum değeri sağlayan sira = {sira+1}, Sayı ise {listeTum[sira]}')



def saniyeCevir(saniye):
    if saniye > 3600:
        saat = saniye // 3600
        
        kalan = saniye - saat*3600
        
        dakika = kalan // 60
        
        kalan = kalan - dakika*60
        
        return(f'\t{round(saat)} saat, {round(dakika)} dakika, {int(kalan)} saniye..')
    if saniye > 60:
        dakika = saniye // 60
        kalan = saniye - dakika*60
        return(f'\t{round(dakika)} dakika, {int(kalan)} saniye..')

    return(f'\t{int(saniye)} saniye..')

