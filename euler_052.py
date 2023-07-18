import time
import itertools
from kullanislimodullerim import *
    
def euler52():
    '''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
        Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''
    
    def duzenle(sayiListesi):
        listeYeni = []
        for sayi in sayiListesi:
            sayi = str(sayi)
            listeYeni.append(sorted(sayi))
        return True if all((x == listeYeni[0] for x in listeYeni)) else False


    def tanila():
        sayi = 1
        while True:
            sayi +=1
            aL = [basamakSayisi(sayi*i) for i in range(1,7)]
            sL = [i*sayi for i in range(1,7)]
            if all((x == aL[0] for x in aL)) and duzenle(sL):
                return sayi,sL
            if sayi == 10**6:
                print('BULUNAMADI...')
                break
    print(tanila())

