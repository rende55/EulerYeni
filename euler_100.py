# PROBLEM NO.100
'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, 
it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.
'''
import time
# ------------------------------------------------------------------------------------------------

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

tum = 10**12
mavi = tum - 10**11
while True:
    sonuc = (mavi/tum)*((mavi-1)/(tum-1))
    if mavi % 10**10 == 0:
        print(f'tüm diskler = {tum},mavi diskler = {mavi} süre = {saniyeCevir(time.process_time())}')
    if sonuc == 1/2:
        print(f'mavi sayısı = {mavi} tüm diskler = {tum}, süre = {saniyeCevir(time.process_time())}')
        break
    if sonuc > 1/2:
        mavi -= 1
    if sonuc < 1/2:
        tum = tum+1
        mavi = tum-10**11



