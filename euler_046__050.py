import time
from kullanislimodullerim import *
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(1_000)

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
    







'''
def e50_CGPTFull():
    # İlk olarak asal sayıları hesaplayan bir fonksiyon yazalım
    def get_primes(n):
        primes = [2]
        for num in range(3, n+1, 2):
            is_prime = True
            for i in range(3, int(num**0.5)+1, 2):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes
            
    # Artan n değeriyle ardışık asal sayılarının toplamını hesaplayan bir fonksiyon yazalım
    def consecutive_primes_sum(sayi):
        a = 100
        max_n = 0
        max_sum = 0
        primes = get_primes(sayi) # 10.000'e kadar olan asal sayıları hesapla
        i = 0
        
        while primes[i] <= a:
            summ = primes[i] + primes[i+1] # Ardışık asal sayılarla başla
            for j in range(i+2, len(primes)):
                summ += primes[j] # Bir sonraki asal sayıyı dene
                if summ >= sayi:
                    break
                if summ in primes and j-i+1 > max_n:
                    max_n = j-i+1
                    max_sum = summ
            i += 1
        return max_n, max_sum
        
    # Test işlemi
    print(consecutive_primes_sum(1_000_000))
'''



#euler46()
#euler47()
#euler48()
#euler49()
euler50()

#e50_CGPTFull()


    
