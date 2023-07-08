import time
import logging
'''
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.

'''
logging.basicConfig(filename="071.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

dT = range(2,1_000_001)
#nSon = d//2 + 1


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

def aralarinda_asal(pay,payda):
    bolenler_n = bolenler(payda)
    for bolen in bolenler_n:
        if pay < bolen:
            return True
        if pay % bolen == 0:
            return False
    return True

'''
for payda in range(2,9):
    for pay in range(1,payda):
        print(pay,payda,aralarinda_asal(pay,payda),sep='\t ----> \t')


'''

tBas = time.time()
maksDeg = 2/5
x = 2/5
y = 3/7
for d in dT:
    if d % 5000 == 0:
        a = saniyeCevir(time.time()-tBas)
        logging.warning(f'{d} sayısına bakılıyor..., süre: {a}')

    nSon = int(d//2 + 1)

    for n in range(1,nSon):
        if n/d < maksDeg:
            continue 
        if n/d >= y:
            break
        if aralarinda_asal(n,d):
            if maksDeg < (n/d):
                maksDeg = n/d
                deg = (n,d)
                logging.warning(f'Yeni değer {n}/{d}, {maksDeg}')

(n,d) = deg
logging.warning(f'Son değer = {n}/{d}, {maksDeg}')


print(saniyeCevir(time.time()-tBas))
