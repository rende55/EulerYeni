#hyperexponentiation 188
#istenen asiriustlusayi(1777,1855) % 10 ** 8 kaçtır

import time
import logging



logging.basicConfig(filename="188_Hyperexponentiation.log", format='%(asctime)s %(message)s',filemode='w')
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

def basamakSayisi(sayi):
    bS = 0
    while sayi > 0:
        sayi = sayi // 10
        bS += 1
        #print(bS, sayi)
    return bS

def asiriuslusayi(sayi,asirius):
    us = 1
    for au in range(asirius-1):
        us = sayi**us   
    return sayi**us

tt = time.time()

sayi = 1777
aUSon = 1855
modum = 10**8
sayimiz =1777


while aUSon > 0:
    kalan = (sayi**sayimiz) % modum
    sayi = kalan
    aUSon -= 1
print(sayi)

'''
for i in range(1,3):
    x = asiriuslusayi(sayimiz,i)
    kalan = x%10**8
    bS= basamakSayisi(x)
    logging.warning(f'{sayimiz} || {i} , basamak sayısı : {bS} , kalan = {kalan}')
    logging.warning(f'sayı: {x}')
'''
print(saniyeCevir(time.time() - tt))
