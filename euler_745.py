# PROBLEM NO.745
'''


For a positive integer,n , define g(n) to be the maximum perfect square that divides n.
For example, , .

Also define
For example,g(18)=9  and g(19) = 1 .

Find S(10**14). Give your answer modulo 10**9 + 7.



'''
import time
import copy
import logging


logging.basicConfig(filename="745.log", format='%(asctime)s %(message)s',filemode='w')
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

def tam_kare_mi(sayi):
    karesi = sayi**0.5
    if karesi == int(karesi):
        return True
    return False
#print(tam_kare_mi(1))

def mukemmel_kare(n):
    if tam_kare_mi(n):
        return n
    for i in range(n//2 +1,0,-1):
        if n%i != 0:
            continue
        if tam_kare_mi(i):
            return i
    return('bir yanlışlık olmalı')


def kareler_toplami(n):
    toplam = 0
    modS    = (10**9)+7
    for i in range(1,n+1):
        mK = mukemmel_kare(i)%modS
        toplam = (toplam+mK)%modS
        if i % 8**6 == 0:
            t = time.process_time()
            logging.warning(f'devam ediyore, {i}, {saniyeCevir(t)}')
            logging.warning(f'g({i}) = {mK}, s({i}) = {toplam}')
    return toplam

tO = kareler_toplami(10**14)
logging.warning(f'S(10**14) = {tO}')