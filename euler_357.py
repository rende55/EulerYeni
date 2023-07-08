# PROBLEM NO.357
'''


Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.



'''
import time
import logging


logging.basicConfig(filename="357-2.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)



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

def bolenler(sayi):
    ox = []
    for i in range(1,sayi//2+1):
        if i > sayi/i :
            break
        if sayi%i==0:
            if i == sayi/i:                  #kalan yoksa i ile sadeleşebilir.. 
                ox.append(i)
            else:
                #ox.append(int(sayi/i))      # sonrakileri denemek iki kere yapmak demek o yüzden kaldırıp denemek yeterli olabilir...
                ox.append(i)
    ox.sort()
    return ox

print(bolenler(30))

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

def sagliyor_mu(n):
    bolenlerN = bolenler(n)
    for d in bolenlerN:
        dene = d + (n/d)
        if asal_mi(dene):
            continue
        else:
            return False
    return True


toplam = 0
tilki = time.time()
for n in range (1,100_000_000):
    if n % 10**4 == 0:
        t = saniyeCevir(time.time()-tilki)
        logging.warning(f' {n} sayısı kontrol ediliyor. süre = {t}')
    if sagliyor_mu(n):
        toplam += n
logging.warning(toplam)
logging.warning(saniyeCevir(time.time()-tilki))
