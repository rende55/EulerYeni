import time
import logging
'''
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	        Relatively Prime	        φ(n)	        n/φ(n)

2	        1	                        1	            2
3	        1,2	                        2	            1.5
4	        1,3	                        2	            2
5	        1,2,3,4	                    4	            1.25
6	        1,5	                        2	            3
7	        1,2,3,4,5,6	                6	            1.1666...
8	        1,3,5,7	                    4	            2
9	        1,2,4,5,7,8	                6	            1.5
10	        1,3,7,9	                    4	            2.5


It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.


'''
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

def bolenler(sayi):
    ox = []
    for i in range(2,sayi//2+1):
        if sayi%i==0:                  #kalan yoksa i ile sadeleşebilir.. 
            ox.append(i)
    return ox

def phi(n):
    bolenler_n = bolenler(n)
    aralarindaAsalListesi = [1] # 1'i eklemek zorundayız
    for sayi in range(2,n):
        for bolen in bolenler_n:
            if sayi % bolen == 0:
                break                           # bölen döngüsünden çık diğer sayıya geç
        else:
            aralarindaAsalListesi.append(sayi)  # hiç bölen yoksa aralarında asal demektir.
    return len(aralarindaAsalListesi)           # sayısını ver

def chi(n):
    if n%2==0:
        asSay = 1
    else:
        asSay = 2
    bol = bolenler(n)
    for sayi in range(3,n):
        for bolen in bol:
            if sayi < bolen:
                asSay += 1
                break
            if sayi % bolen == 0:
                break
        else:
            asSay += 1
    return asSay

for i in range(2,11):
   print(i,chi(i))

maksDeger = 0
tBas = time.time()
for i in range(2,1_000_001):
    if i % 10_000 == 0:
        print(i,saniyeCevir(time.time()-tBas))
    fi = phi(i)
    if i/fi > maksDeger:
        maksDeger = i/fi
        deger = i
print(maksDeger,deger)
print(saniyeCevir(time.time()-tBas))
