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



def euler54():
    # ----------------------------------------------- import vs.... -------------------------------------------------------------------#
    with open("p054_poker.txt", 'r') as liste1:     #listemizi dosyadan çekiyoruz.
        lines = liste1.read().splitlines()

    # ----------------------------------------------- datalar....   -------------------------------------------------------------------#
    kartlar = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    renkler = ['C', 'D', 'S', 'H']
    elDeger = ['HC', 'OP', 'TP', 'TK', 'S0', 'F0','FH','FK','SF', 'RF'] 

    # ----------------------------------------------- ana fonksiyonlar   -----------------------------------------------------------------#

    def f1_cevir(listem,yeniliste=[]):
        for eleman in listem:
            eleman = eleman.split(' ')
            pl1 = eleman[0:5]
            pl2 = eleman[5:10]
            yeniliste.append([pl1,pl2])
        return yeniliste

    def f2_sirala(el):
        el_sirali = sorted(el, key=lambda card: kartlar.index(card[0]))
        return el_sirali

    def f3_kiyasla(oyun):
        player  = [0,0] 
        plHC    = [0,0]
        
        for sira, oyuncu in enumerate(oyun):
            birli,ikili,uclu,dortlu, pairdeger = d3_degersay(oyuncu)
            oyuncu = f2_sirala(oyuncu)
            yuksek_kart_ind = kartlar.index(d4_yüksekkart(oyuncu))
            #print(f'{sira+1}. oyuncunun eli: {oyuncu}\n')
            if d1_aynirenkmi(oyuncu) and d2_siralimi(oyuncu):
                if yuksek_kart_ind      == 12:
                    #print(f'{sira+1}. oyuncu el değeri Royal Flush!')
                    player[sira]        = 10
                else: 
                    #print(f'{sira+1}. oyuncu el değeri Straight Flush!')
                    player[sira]        = 9
            if d1_aynirenkmi(oyuncu) and d2_siralimi(oyuncu) == False:
                #print(f'{sira+1}. oyuncu el değeri Flush!')
                player[sira]            = 6
            if d1_aynirenkmi(oyuncu)    == False:
                if d2_siralimi(oyuncu) and birli ==5:
                    #print(f'{sira+1}. oyuncu el değeri Straight!')
                    player[sira]        = 5
                    plHC[sira]          = yuksek_kart_ind
                elif dortlu             == 1:
                    #print(f'{sira+1}. oyuncu el değeri Four of a Kind!')
                    player[sira]        = 8
                    plHC[sira]          = pairdeger
                elif uclu               == 1:
                    if ikili            == 1:
                        #print(f'{sira+1}. oyuncu el değeri Full House!')
                        player[sira]    = 7
                        plHC[sira]      = pairdeger                   
                    else:
                        #print(f'{sira+1}. oyuncu el değeri Three of a Kind!')
                        player[sira]    = 4
                        plHC[sira]      = pairdeger
                elif ikili              == 2:
                    #print(f'{sira+1}. oyuncu el değeri Two Pair!')
                    player[sira]        = 3
                    plHC[sira]          = pairdeger
                elif ikili              == 1:
                    #print(f'{sira+1}. oyuncu el değeri One Pair!')
                    player[sira]        = 2
                    plHC[sira]          = pairdeger
                else:
                    #print(f'{sira+1}. oyuncu el değeri High Card!')
                    player[sira]        = 1
                    plHC[sira]          = yuksek_kart_ind

        player1 = player[0]
        player2 = player[1]
        hC1 = plHC[0]
        hC2 = plHC[1]
        if player1 < player2:
            #print(f'\t ...eli 2. oyuncu kazandı')
            return 'Oyuncu-2'
        if player1 > player2:
            #print(f'\t ...eli 1. oyuncu kazandı')
            return 'Oyuncu-1'
        if player1 == player2:
            #print('\t ...el değerleri eşit')
            if hC1 < hC2:
                #print(f'\t ...eli {hC2} ile 2. oyuncu kazandı')
                return 'Oyuncu-2'
            elif hC1 > hC2:
                #print(f'\t ...eli {hC1} ile 1. oyuncu kazandı')
                return 'Oyuncu-1'
            else:
                #print('\t ...el değerleri eşit')
                return oyunsayaci


    # ----------------------------------------------- yardımcı fonksiyonlar ----------------------------------------------------------------#
    def d1_aynirenkmi(liste):
        elrengi = set()
        for el in liste:
            elrengi.add(el[1])
        if len(elrengi) == 1:
            #print('Hepsi aynı renk = ')
            return True
        else:
            return False
     
    def d2_siralimi(liste):
        liste = f2_sirala(liste)
        ilk_indis = kartlar.index(liste[0][0])
        son_indis = kartlar.index(liste[-1][0])
        if son_indis - ilk_indis != 4:
            #print('sirali değil')
            return False
        else:
            #print('siralidir. en yüksek kart : ', son_indis)
            return son_indis

    def d3_degersay(liste):
        listem = list(i[0] for i in liste)
        degerler = list()
        for i in set(listem):
            degerler.append(listem.count(i))
        listem = list(set(listem))
        liste_tem = list()
        liste_tem.append(listem)
        liste_tem.append(degerler)
        birli   = degerler.count(1)
        ikili   = degerler.count(2)
        uclu    = degerler.count(3)
        dortlu  = degerler.count(4)

        if dortlu   == 1:
            indis   = liste_tem[1].index(4)
            kart    = liste_tem[0][indis]
            deger   = kartlar.index(kart)
        if uclu     == 1:
            indis   = liste_tem[1].index(3)
            kart    = liste_tem[0][indis]
            deger   = kartlar.index(kart)
        if ikili    == 1:
            indis   = liste_tem[1].index(2)
            kart    = liste_tem[0][indis]
            deger   = kartlar.index(kart)
        if ikili    == 2:
            deger   = 0
            for ara in liste_tem[1]:
                if ara          == 2:
                    indis       = liste_tem[1].index(2)
                    kart        = liste_tem[0][indis]
                    atama       = kartlar.index(kart)
                    if deger    < atama:
                        deger   = atama
        if birli    == 5:
            deger = 'tanımsız'

        return birli,ikili,uclu,dortlu,deger

    def d4_yüksekkart(liste):
        #liste = f2_sirala(liste)
        yüksek_kart = liste[4][0]
        #print('Yüksek Kart : ', yüksek_kart )
        return yüksek_kart


    # -------------------------------------------------------- işlemler ---------------------------------------------------------------------#

    oyunListesi2 = f1_cevir(lines)
    oyunsayaci = 0
    oyuncu_1 = 0
    oyuncu_2 = 0
    esitlik = 0
    esitoyun = []
    for oyunlar in oyunListesi2:
        oyunsayaci +=1
        kazanan = f3_kiyasla(oyunlar)
        #print(f'\n\n --------------------------------------{oyunsayaci}. oyun ------------------------------------------ \n')
        if kazanan == 'Oyuncu-1':
            oyuncu_1 += 1
        elif kazanan == 'Oyuncu-2':
            oyuncu_2 += 1
        else:
            esitlik +=1
            esitoyun.append(kazanan)

    print ('\n\n --------------------------------------------------------------------------------------\n')
    print(f' Sonuç\n\t1.Oyuncu = {oyuncu_1} \n\t2. Oyuncu = {oyuncu_2} \n\tBeraberlik = {esitlik}')
    print ('\n\n --------------------------------------------------------------------------------------\n')
    print('\t eşit oyun = \t', esitoyun )


#euler51()
euler52()
#euler54()