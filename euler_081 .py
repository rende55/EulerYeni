# PROBLEM NO.81
'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.
a = 
'131,673,234,103,18
201, 96, 342, 965, 150
630, 803, 746, 422, 111
537, 699, 497, 121, 956 
805, 732, 524, 37, 331'


Find the minimal path sum from the top left to the bottom right by 
only moving right and down in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing an 80 by 80 matrix.

'''
import time
import copy
import logging
from itertools import *

matris5 = [
    [131, 673, 234, 103, 108],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331]] 


with open("p081_matrix.txt", 'r') as liste1:     #listemizi dosyadan çekiyoruz.
    lines = liste1.read().splitlines()
matris80 = list()
for eleman in lines:
    eleman = eleman.split(',')
    matris80.append(eleman)

for satir in matris80:
    for indis, deger in enumerate(satir):
        satir[indis] = int(deger)

# ------------------------------------------------------------------------------------------------


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

def min_toplam(ucgen):
    yol_uzunlugu = len(ucgen)
    seviye = len(ucgen)-1
    yollar  = [[] for i in range(len(ucgen[-1]))] # tek hamlede doğru yaptık ya la
    for ax in range(len(ucgen[-1])):
        yollar[ax].append(ucgen[-1][ax])
    print(f'toplam {yol_uzunlugu} katman bulunmaktadır.\n')
    yeniyollar = []
    while seviye > 0:    
        yeniyollar = []
        gecici_liste = []
        #print(f'---------------------------------------------------------------\n\t{seviye}. katman inceleniyor...\n')
        
        altliste = ucgen[seviye-1]
        for indeks, deger in enumerate(altliste):
            #print(f'\n\t değer : {deger}, sıra: {indeks}.. \nEşleşme {indeks} ve {indeks+1} ile olabilir...')   
            if sum(yollar[indeks]) < sum(yollar[indeks+1]):
                #print (f"birinci yol daha küçük,  {deger}, {yollar[indeks]}'e aktarılıyor...")
                gecici_liste = copy.deepcopy(yollar[indeks])
                gecici_liste.insert(0,deger)
                #print(gecici_liste)           
            elif sum(yollar[indeks]) > sum(yollar[indeks+1]):
                #print (f"ikinci yol daha küçük,  {deger}, {yollar[indeks+1]}'e aktarılıyor...")
                gecici_liste = copy.deepcopy(yollar[indeks+1])
                gecici_liste.insert(0,deger)
                #print(gecici_liste)    
            else:
                #print("HATA ! iki yol eşit. herhangi biri seçiliyor ")
                gecici_liste = copy.deepcopy(yollar[indeks+1])
                gecici_liste.insert(0,deger)
                #print(gecici_liste)
            yeniyollar.append(gecici_liste)
        yollar = copy.deepcopy(yeniyollar)
        #print(yeniyollar)
        print(f'\n\t{seviye}. katman incelenmesi tamamlandı...\n ---------------------------------------------------------- \n')
        seviye -=1
    print(sum(yeniyollar[0]), yeniyollar,sep='\n\t')
    return
        
def karo_yap(matris):
    print('Matris Karoya dönüştürülüyor.......')
    xSon = len(matris)          #5
    ySon = len(matris[0])       #5  
    (x,y) = (0,0)
    asama = 0
    asamaSon = 2*xSon - 1       #9
    listem = [[(0,0)]]
    while asama != asamaSon-1:
        geciciListem = set()
        for (x,y) in listem[asama]:
            if x < xSon-1:
                geciciListem.add((x+1,y))
            if y < ySon-1:
                geciciListem.add((x,y+1))
        geciciListem = list(geciciListem)
        listem.append(geciciListem)
        asama += 1
    print('\t\t\t\t\t DONE.\n\n')

    for l in listem:
        for index, (x,y) in enumerate(l):
            l[index] = matris[x][y]

    return listem

def ucgen_yap(karo):
    print('Karo üçgene dönüştürülüyor.......')
    uzunluk = len(karo)                     # 5 için 9
    ortaIndis = int((uzunluk - 1)/2)             # orta indis = 4
    s = ortaIndis                           # s = 4
    deg = len(karo[s])                      # deg = 5
    while s+1 < uzunluk:                      # s < 9 için:
        while len(karo[s+1]) < deg+1:         # 4 < 6 ise
            karo[s+1].append(10000)
            karo[s+1].insert(0,10000)
        deg += 1
        s += 1
    print('\t\t\t\t\t DONE.\n\n')
    return karo

ilkZaman = time.time()
karoN = karo_yap(matris80)
karoNx = copy.deepcopy(karoN)
ucgenim = ucgen_yap(karoNx)
min_toplam(ucgenim)        
print(saniyeCevir(time.time()-ilkZaman))
