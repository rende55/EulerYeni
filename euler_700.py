

'''

Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4.503.599.627.370.517.

An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin. 

The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin.
However, the third term is 8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins

'''
import time
import logging
from kullanislimodullerim import *


logging.basicConfig(filename="700.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


sabita = 1504170715041707
modTabania = 4503599627370517

def eulercoin_ureteci():
    print('BAŞLA')
    logging.warning('BAŞLA...')
    t2 = time.time()
    sabit = 1504170715041707
    ilksayi = 2573 # DÖNG SONLANDIRILDI BU DEĞER DEĞİŞTİ..
    modTabani = 4503599627370517
    toplam = 1504170715041707 # ilk eleman alınmadan başla
    ds = 1
    nS  = 1
    
    md = ilksayi+sabit
    sonuc = md % modTabani
   


    while True:
        #break
        #print(sonuc)
        ds+=1
        nS+=1
        
        if sonuc < ilksayi:
            print('Yeni coin bulundu...')
            logging.warning(f'Yeni coin...: \t\t\t {sonuc},\nSüre...: {saniyeCevir(time.time()-t2)}, Döngü sayısı..: {ds}, zaman..: {time.asctime()},  toplam döngü..: {nS}\n')
            toplam += sonuc
            ilksayi = sonuc
            ds = 0
            md += ilksayi
            sonuc = md % modTabani
            continue    
        if sonuc in [0,1]:
            print('COIN UReTIMI BITTI..')
            logging.warning('COIN UReTIMI BITTI..')
            break
        else:
            md += sabit
            sonuc = md % modTabani

        
        #print(sonuc)
    logging.warning(f'COIN UReTIMI BITTI.. toplam = {toplam}')
    return toplam
    
    '''

    '''



#print(saniyeCevir(time.time() - tt))
print(eulercoin_ureteci())










