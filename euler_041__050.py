import time
from kullanislimodullerim import *
import sys
sys.setrecursionlimit(1_000)



def euler41():

    #listem = [i for i in range(1,10)]

    #print(listem)
    #print(f'\t {len(listem)} basamaklı sayılar deneniyor....')
      
    def basamak_sayisini_bul(sayi):
        basamakSayisi = 0
        if sayi / 10 < 1 :
            basamakSayisi = 1
            return basamakSayisi

        while sayi > 1:
            basamakSayisi += 1
            sayi = sayi / 10
        return basamakSayisi
    '''
    print(basamak_sayisini_bul(19765243))
    print('BİTTİ')    
    '''
    def pandijital_mi(sayi):
        for i in range(1,basamak_sayisini_bul(sayi)+1):       # 1 ile basamak sayısı arası 4 bs -> 1,2,3,4
            if str(sayi).count(str(i)) == 1:
                continue
            else:
                return False
        return True

    def asal_mi(sayi):
        if sayi == 0 or sayi == 1:
            return False
        karekok = int(round(sayi**0.5))
        #print(karekok)
        for a in range(2,karekok+1):
            if sayi % a == 0:
                return False
            else:
                continue
        else:
            return True
    


    a = 0
    t1 = time.time()
    for i in range(987654321,10,-2):
        a += 1
        #if a % 10000 == 0:
        #    print(f'{a}. sayı deneniyor...')
        #    pass
        if pandijital_mi(i):
            #print(f'\n pandijital bulundu: \t\t\t {i} .',end='',flush=False)
            if asal_mi(i):
                #print('')
                #print('\t\t\t asal da bulundu....\n')
                print(i)
                break
    t2 = time.time()
    print((t2 - t1)//60, 'dakika sürdü')
    '''
    for i in range(987654322,1,-1):
        a += 1
        print(f'{a}. sayı deneniyor...')
        if asal_mi(i):
            print(f'\n asal bulundu \n\n \t\t\t {i}')
            if pandijital_mi(i):
                print('')
                print('\t\t\t bulundu....\n')
                print(i)
                break
    '''
def euler42():
    '''
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position
    and adding these values we form a word value. For example, the word value 
    for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
    Using words.txt (right click and 'Save Link/Target As...'), 
    a 16K text file containing nearly two-thousand common English words, 
    how many are triangle words?
    
    
    
    
    
    
    '''
    harfler = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ucgenDeger = [int(n*(n+1)/2) for n in range(1,1000)]
    #print(ucgenDeger)

    
    lines = list()
    with open('p042_sozcukler.txt') as file:
        for line in file:
            line = line.replace('"','')
            line = line.split(',')
            lines.append(line)
        kelimeler = lines[0]
    def kelime_degeri(kelime):
        deg = 0
        for harf in kelime:

            hd = harfler.index(harf) + 1
            #print(f'harf: {harf}, değeri: {hd}.. ')
            deg += hd
        return deg

    sayac = 0
    for kelime in kelimeler:
        if kelime_degeri(kelime) in ucgenDeger:
            sayac+=1

    print(sayac)
def euler43():
    '''
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
    but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    
    '''
    def pandijital_mi(sayi):
        for i in range(10):       # 1 ile basamak sayısı arası 4 bs -> 1,2,3,4
            if str(sayi).count(str(i)) == 1:
                continue
            else:
                return False
        return True
    
    def ikinci_sart(sayi):
        sayiStr = str(sayi)
        a,b = 0,3
        listeB = [2,3,5,7,11,13,17]

        for bolen in listeB:
            a = a+1
            b = b+1
            sayi = int(sayiStr[a:b])
            if sayi%bolen != 0:
                return False
        return True    
    toplam = 0
    print(pandijital_mi(1406357289))
    st = 1406357289
    print(str(st)[5])
    for i in range(1023456789,9876543211):
        if int(str(i)[5]) % 5 != 0:
            continue
        if int(str(i)[3]) % 2 != 0:
            continue
        if pandijital_mi(i):
            #print(f'{i} sayısı pandijitaldir. ikinci şart aranıyor...')
            if ikinci_sart(i):
                toplam +=i
                print(f'\tiki şart da sağlandı. {i} sayısı toplama ekleniyor... toplam = {toplam}')
                    
    print(f'SON TOPLAM = {toplam}')
def euler44():
    '''
    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
    '''
    def pentagonal(n):
        return int(n*(3*n - 1)/2)
    
    print(pentagonal(2167)-pentagonal(1020))

    pList = []
    for i in range(10000):
        pList.append(pentagonal(i))
    #print(pList)

    for a in pList:
       
        if a == 0:
            continue
        for b in pList:
            if b == 0 or a>=b:
                continue
            if a+b in pList:
                if b-a in pList:
                    print(f'P({pList.index(a)}) = {a}, P({pList.index(b)}) = {b}, P({pList.index(a+b)}) = {a+b}')
                    break
        else:
            continue
        break  

    else:
        print('BULUNAMADI..')

def euler46():

    def kare_mi(sayi):
        x = sayi**(1/2)
        if x == int(x):
            return True
        else:
            return False 

    

    sayi = 31
    while True:

        if asal_mi(sayi):
            sayi+=2
            continue

        for i in range(2,sayi):
            if asal_mi(i):
                dene = (sayi-i)/2
                if kare_mi(dene): 
                    sayi+=2 #koşul sağlandı...
                    break 
                else:
                    continue
        else:
            print(f'Sayı Bulundu... Sayımız = {sayi}')    
            break
def euler47():
    def asal_ls(sonAsal):
        liste1 = [2,3]
        s = 4
        while s <= sonAsal:
            for i in liste1:
                if s % i == 0:
                    s +=1
                    break
                else:
                    continue
            else:
                liste1.append(s)
                s +=1
        return liste1

    print(asal_ls(35)[-1])


    def asal_carpanlar(sayi):
        asalCarpan = []
        if sayi%2==0:
            asalCarpan.append(2)
        for i in range(3,(sayi//2)+1,2):
            #if asal_mi(i):
            if i in asal_ls(i):
                if sayi%i == 0:
                    asalCarpan.append(i)
        return asalCarpan
    
    sayimiz = 5
    tbas = time.time()
     
    uskok = 1
    pS = 0
    while True:
        if sayimiz == 255_000:
            print('reached maximum number')
            break
        '''
        if asal_mi(sayimiz):
            pS = 0
            sayimiz +=1
            continue
        '''
        if pS == 4:
            print('buldum...')
            print('SONUÇ   :  ', sayimiz-4)
            break
        if sayimiz % 5**uskok == 0 :
            tAra = time.time()
            print(sayimiz,'\t\t...... süre      :\t', round(tAra-tbas), '    sn')
            uskok += 1
        if len(asal_carpanlar(sayimiz)) == 4:
            #print(sayimiz,asal_carpanlar(sayimiz))
            pS+=1
            sayimiz +=1
        else:
            pS = 0
            sayimiz += 1
            #print('')
            
    tson=time.time()
    print(tson-tbas)
def euler48():
    def islem(sayi):
        return (sayi**sayi)%(10**11)
    topla = 0
    for i in range(1,1001):
        topla += islem(i)
    print(topla%10**11)
def euler49():
    def perm_mi(sayi):
        sayi2 = sayi+3330
        sayi3 = sayi2+3330
        liste1 = list(str(sayi))
        liste2 = list(str(sayi2))
        liste3 = list(str(sayi3))
        if not asal_mi(sayi2) or not asal_mi(sayi3):
            return False
        if liste1 == liste2 or liste1 == liste3 or liste2==liste3:
            return False
        if sorted(liste1) != sorted(liste2) or sorted(liste1) != sorted(liste3) or sorted(liste3) != sorted(liste2):
            return False
        print(str(sayi)+str(sayi2)+str(sayi3))
        return True
    for say in range(1111,10000):
        if asal_mi(say):
            perm_mi(say)
        else:
            continue
def euler50():

    # ÇALIŞIYOR AMA 1 M İÇİN YAVAŞ 
    def maks_hesapla(baslangic,sayi):
        #print(f'TOPLAMust = {toplam}')
        
        for i in range(baslangic,sayi):
            toplam  = 0
            dizi    = 0
            for asal in asal_uret(i,sayi):
                toplam  += asal
                dizi    += 1
                if toplam < sayi:
                    continue
                elif toplam == sayi: # en uzun seri en baştakilerden bulunca biter..
                    #print(f'SAYI:{sayi} \t SIRA:{dizi} \t TOPLAM:{toplam}, BULUNDU..son Asal = {asal}')
                    return sayi, dizi
                else:
                    break #recursive derinliği yetmedi..
        else:
            return sayi,0

    def maks_bul(sunaKadar):
        t1 = time.time()
        maks,makd = 0,0
        for bakilanAsal in asal_uret(2,sunaKadar):
            a,b = maks_hesapla(2,bakilanAsal)
            if b > makd:
                maks,makd = a,b
                t2 = time.time()
                print(f'Yeni Lider..  {maks}, \t\t sıra sayısı.. {makd}, süre: {saniyeCevir(t2-t1)}')
        return maks,makd 


   # ÇALIŞIYOR AMA 1 M İÇİN daha YAVAŞ      
    def listeden_hesapla(sayi):
        t1 = time.time()
        listeAsal = list(asal_uret(2,sayi))
    
        maxSayi, maxDizi = 0,0
        for asalSayi in listeAsal:
            listye = listeAsal[:listeAsal.index(asalSayi)//2 + 1] #Sıradaki asaldan itibaren alt kümeyi seç
            #print(asalSayi, listye)
            for i in range(len(listye)+1):
                for y in range(len(listye)+1):
                    if i >=y+maxDizi:
                        continue
                    else: 
                        lAlt = listye[i:y]
                        #print(i,y,lAlt,listye,asalSayi,sep='\t\t') #0:5
                        #print(lAlt,listye,sep='\t\t')
                        altToplam = sum(lAlt)
                        if altToplam == asalSayi: 
                            #print(asalSayi,len(lAlt),lAlt)
                            if len(lAlt) > maxDizi:
                                t2 = time.time()
                                print('Yeni Lider',maxSayi, maxDizi,saniyeCevir(t2-t1) )
                                maxDizi,maxSayi = len(lAlt), asalSayi
                            continue
                    
        return maxSayi, maxDizi
    
    def bularak_ilerle(sayi):
        
        maxToplam,maxDizi = 0,0
        toplam = 0
        t1 = time.time()
        #toplam bulacağımız için yarısını alabiliriz. 1 milyonun yarısına kadar toplayarak ilerle ve toplam asal mı sorgula..
        for i in range (2,sayi//2):
            dizi = 0
            toplam = 0
            for asalS in asal_uret(i,sayi//2+1):
                toplam = toplam+asalS
                #print(toplam)
                if toplam > sayi:
                    #print(f'burda bitti{sayi}')
                    break
                dizi += 1
                if asal_mi(toplam):
                    if dizi > maxDizi:
                        t2 = time.time()
                        maxDizi,maxToplam = dizi, toplam
                        print(f'Yeni Lider..  {maxToplam}, \t\t sıra sayısı.. {maxDizi}, süre: {saniyeCevir(t2-t1)}')
                        continue
                    continue

                
            
        return maxDizi,maxToplam
    
    #print(listeden_hesapla(10**6))
    #print(maks_bul(10**6))
    print(bularak_ilerle(10**6))

