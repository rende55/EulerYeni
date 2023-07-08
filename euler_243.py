import time
import logging
'''
A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), 
to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
'''
def cift_mi(sayi):
    if sayi%2 == 0:
        return True
    else:
        return False
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

def bolenler(payda):
    ox = []
    for i in range(2,payda//2+1):
        if payda%i==0:                  #kalan yoksa i ile sadeleşebilir.. 
            ox.append(i)
    return ox

def esneklikCift():
    print('işlem başladı... sadece çiftler deneniyor')
    logging.basicConfig(filename="testOnluSayilar.log", format='%(asctime)s %(message)s',filemode='w')
    #logging.basicConfig(filename="KAYIT_deneme_4.log", format='%(asctime)s %(message)s',filemode='w')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)
    t1 = time.time()
    tAra = time.time()
    # 6.469.693.230
    print('devam ediyor...')
    n = 0
    while n < 6000002:
        n+=223092870
        payda = n*4
        esneklikpuani = 1
        bolenlerPayda = bolenler(payda)
        
        for pay in range(2,payda):
            for bolen in bolenlerPayda:
                if pay<bolen:               # kendinden büyük bölenleri denemeye gerek yok. bu noktaya kadar döngü devam ettiyse orda kesiliyor.
                    esneklikpuani+=1
                    break 
                if pay % bolen == 0:
                    break
                else:
                    continue
            else:
                esneklikpuani +=1           # kendinden büyük bölen yok ve hiçbir bölene tam bölünmüyorsa bu noktaya ulaşıyoruz.
        else:
            if esneklikpuani/(payda-1) < 15499/94744:
                print('bulundu, işlem sonu.')
                logging.warning(f'R({payda}) = {esneklikpuani}/{payda-1} = {esneklikpuani/(payda-1)} , süre = {saniyeCevir(time.time()-t1)} ')
                return
            else:
                logging.warning(f'R({payda}) = {esneklikpuani}/{payda-1} = {esneklikpuani/(payda-1)} , süre = {saniyeCevir(time.time()-t1)} ')
                continue
               
    else:
        print('bulunamadı, işlem sonu.')
        logging.warning(f' BULUNAMADI.. süre = {saniyeCevir(time.time()-t1)} \n ')  
        return

def esneklikTek():
    print('işlem başladı... sadece tekler deneniyor')
    logging.basicConfig(filename="testTekSayilar.log", format='%(asctime)s %(message)s',filemode='w')
    #logging.basicConfig(filename="KAYIT_deneme_4.log", format='%(asctime)s %(message)s',filemode='w')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    t1 = time.time()
    tAra = time.time()
    print('devam ediyor...')
    for payda in range(10_000_001,10_000_202,2):
        #if asal_mi(payda):
        #    continue ################# yeni 2108 - 01:11
        esneklikpuani = 1
        bolenlerPayda = bolenler(payda)
        for pay in range(2,payda):
            #if payda%2==0 and pay%2==0:
            #    continue                #ikisi de çift ise deneme
            for bolen in bolenlerPayda:
                if pay<bolen:               # kendinden büyük bölenleri denemeye gerek yok. bu noktaya kadar döngü devam ettiyse orda kesiliyor.
                    esneklikpuani+=1
                    break ########## yeni
                if pay % bolen == 0:
                    break
                else:
                    continue
            else:
                esneklikpuani +=1           # kendinden büyük bölen yok ve hiçbir bölene tam bölünmüyorsa bu noktaya ulaşıyoruz.
        else:
            if esneklikpuani/(payda-1) < 15499/94744:
                print('bulundu, işlem sonu.')
                logging.warning(f'R({payda}) = {esneklikpuani}/{payda-1} = {esneklikpuani/(payda-1)} , süre = {saniyeCevir(time.time()-t1)} ')
                return
            else:
                logging.warning(f'R({payda}) = {esneklikpuani}/{payda-1} = {esneklikpuani/(payda-1)} , süre = {saniyeCevir(time.time()-t1)} ')
                continue
    else:
        print('bulunamadı, işlem sonu.')
        logging.warning(f' BULUNAMADI.. süre = {saniyeCevir(time.time()-t1)} \n ')  
        return



esneklikCift()
#esneklikTek()