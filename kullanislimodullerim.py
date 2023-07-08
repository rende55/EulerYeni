import time
from itertools import *



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

def asal_mi(sayi):
    if sayi < 2:
        return False
    if sayi == 2:
        return True
    kk = sayi**0.5  
    kk = round(kk)
    
    for i in range(2,kk+1):
        if sayi % i == 0:
            return False
        else:
            continue
    else:
        return True

def basamakSayisi(sayi):
    bS = 0
    while sayi > 0:
        sayi = sayi // 10
        bS += 1
        #print(bS, sayi)
    return bS

def obeb(sayi1,sayi2):
    kucukSayi = sayi1
    buyukSayi = sayi2
    if sayi1>sayi2:
        kucukSayi,buyukSayi = sayi2,sayi1

    a = 2
    obeb = 1
    while buyukSayi > 1:
        if buyukSayi % a == 0 or kucukSayi % a == 0: # ikisinden biri bölünüyorsa al
            #print(f'bölen = {a}')
            if buyukSayi % a == 0 :
                buyukSayi = buyukSayi // a
            if kucukSayi % a == 0 :
                kucukSayi = kucukSayi // a
            obeb = obeb*a
        else:
            a = a + 1
    print(f'{sayi1} ile {sayi2} nin obebi {obeb} tir...')
    return obeb

def bolenler(sayi):
    ox = []
    for i in range(2,sayi//2+1):
        if sayi%i==0:                  #kalan yoksa i ile sadeleşebilir.. 
            ox.append(i)
    return ox

def euklid_bolme (a,b):
    x = a%b
    if x == 0:
        return b
    else: 
        return euklid_bolme(b,x)

def asalcarpanlar(sayi):
    #asal_carpanlar = []
    ilk = 2
    for asal in asal_uret(ilk,sayi//2+1):
        #print(asal)
        if sayi%asal==0:
            print(f'asal çarpan = {asal}')
            #asal_carpanlar.append(asal)
            yield asal
            continue    
    #return asal_carpanlar        

def asal_uret(baslangic,bitis):
    for i in range(baslangic,bitis):
        if asal_mi(i):
            yield i

#dg      = 1_504_170_715_041_707/(17*1249*12043)
#modS    = (4_503_599_627_370_517-1)/(2*2*3*3*3*3*23*612229)
#print(asal_mi(modS))
#print(asal_mi(modS))
 