import time
import itertools
from kullanislimodullerim import *
    
def euler51():
    '''
    iki basamaklı sayıların ilk rakamını 3 le değişince 9 sayıdan 6 sı asal sayı oluyor. 13 23 43 53 73 ve 83
    56**3 şeklindeki 5 basamklı sayıların yıldız gelen yere aynı rakam ile değiştirilmesiyle oluşan 10 sayıdan 7 tanesi asal sayı oluyor 56003 56113 56333 56443 56773 56993 56003
    bu 7li grupdaki 56003 bu sayılardan en küçüğüdür.

    aynı şekilde aynı rakamı değiştirilerek oluşturulmuş 8 li asal grup ve bu grubun en küçük sayısını bul.

    '''
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

    def sekizli_bul(grup):
        a = 0
        for sayi in grup:
            if asal_mi(int(sayi)):
                a += 1
        #if a == 7:
        #    print('7 li var')
                #return False
        if a >= 8:
            return True
        return False

    def grup_olustur(sayi,degisecekBasamakSayisi):
        grup = list()                                   # dönüşen sayılar için grup - her grup 10 sayidan oluşacak
        gruplar = list()                                # tüm 10lu gruplar belki lazım olur..
        dBS = degisecekBasamakSayisi                    # kaç basamak aynı rakama dönüşecek
        rakamHavuzu = [str(i) for i in range(0,10)]     # rakam havuzundan sırayla dönüşecek rakamı seçiyoruz 0-9
        sayiSTR = str(sayi)
        deg = len(sayiSTR)                              # sayinin basamak sayisi döngü bitişi için önemli
        # 5 basamağın 2 si değişirse kaç olasılık var (ilk basamak hariç)...
        # (01 02 03 04)<--bunlar alınmıyor. (12 13 14) (23 24) (34) alınacak 0 olanlar iptal edilecek Top 6 olasılık --> C(4,2)
        komb = list(itertools.combinations(range(deg),dBS))   # ilk basamağı değişmiyoruz..
        #print(komb)         ##### TEST ######
        for degisecekler in komb:
            a,b,c = degisecekler                                # bunu da değişken sayısına göre seçilebilir yapabilir miyiz?
            for rakam in rakamHavuzu:
                if a == 0 and rakam == '0':
                    continue
                sayiSTRC = sayiSTR
                sayiSTRC = sayiSTRC[:a]+rakam+sayiSTRC[(a+1):]
                sayiSTRC = sayiSTRC[:b]+rakam+sayiSTRC[(b+1):]
                sayiSTRC = sayiSTRC[:c]+rakam+sayiSTRC[(c+1):]
                
                #sayiSTRC = sayiSTRC[:d]+rakam+sayiSTRC[(d+1):]
                #sayiSTRC = sayiSTRC[:e]+rakam+sayiSTRC[(e+1):]

                grup.append(sayiSTRC)
            #print(grup)
            if sekizli_bul(grup):                           # grup listesini sorgula
                return grup
            grup = []
        return []
    tBaslangic = time.time()
    for i in range(1_000,121_500):        
        #if i % 10_000 == 0:
        #    print(i,'  \t sayısına geldik')
        li = grup_olustur(i,3)
        if li:
            print(li)
            print('sonuç = ', li[0])
            print(time.time() - tBaslangic)
            return
    else:
        print('bulunamadı')
        print(time.time() - tBaslangic)
        return
