# PROBLEM NO.60
'''
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''

# TOPLAMI BELKİ BU DÖRT HARİCİ SAYILAR BELİRLİYOR OLABİLİR

import time
import logging



logging.basicConfig(filename="060.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
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

def birlesim_kontrol(sayi1,sayi2):
    sayibir = int(str(sayi1)+str(sayi2))
    if asal_mi(sayibir):
        sayiiki = int(str(sayi2)+str(sayi1))
        if asal_mi(sayiiki):
            return True
    return False

def asal_uret(adet=0,baslangic=3):
    if baslangic%2==0:
        baslangic +=1
    sayac = 0
    listeAsal = list()
    while sayac < adet:
        if asal_mi(baslangic):
            listeAsal.append(baslangic)
            sayac+=1
    return listeAsal


ilkZaman = time.time()
dene = 3 #(listem[-1] + 2)
#ekle = 673
#listem = [3]
#dene = (listem[-1] + 2)
#d = 0
#minToplam = 15_000_001
# ---------------------------------------- Motorlar -------------
def ilk_liste():
    sira = 1
    logging.warning(f'{sira}\t---- İlk Liste hazırlanıyor.... ')
    sira+=1
    asalListesi = [3]
    deneme = (asalListesi[-1] + 2)   
    while True: 
        #d +=1
        #if sum(listem)>minToplam:
        #    dene = listem.pop()+2
        if len(asalListesi) == 5:
            break
        #if d % 1_000_000 == 0:
        #    print(f'{d}. deneme',dene, saniyeCevir(time.time()-ilkZaman),sep='\t--->  ')    
        if asal_mi(deneme):
            for asal in asalListesi:
                if birlesim_kontrol(asal,deneme):
                    continue
                else:
                    break
            else:
                asalListesi.append(deneme)
                #break
        deneme+=2 # çiftleri denemesin diye
    logging.warning(f'{sira}\t---- İlk Liste oluşturuldu.... ')
    sira+=1
    logging.warning(f'{sira}\t---- İlk Liste : {asalListesi}.... ')
    sira+=1
    return(asalListesi,sira)

def bese_tamamla(liste,sira,deneme,limit):
    logging.warning(f'{sira}\t---- beşli liste oluşturuluyor .... ')
    sira+=1
    asalListesi = liste 
    while deneme < limit: 
        if len(asalListesi) == 5:
            logging.warning(f'{sira}\t---- beşe tamamlandı. Liste : {asalListesi}....  ')
            sira+=1
            return asalListesi,sira
        if asal_mi(deneme):
            for asal in asalListesi:
                if birlesim_kontrol(asal,deneme):
                    continue
                else:
                    break
            else:
                asalListesi.append(deneme)
        deneme+=2 # çiftleri denemesin diye

    logging.warning(f'{sira}\t---- beşe tamamlanamadi. Liste : {asalListesi}.... ')
    sira+=1
    return asalListesi,sira

liste, sira = [7,19,97,3727,12_592_999],1


logging.warning(f'{sira}\t liste toplami küçültülüyor..')
sira+=1
denemeSayisi    = 0
listeUzunlugu   = len(liste)            #5
sonEleman       = liste[-1]             #129_976_621
#denenen         = sonEleman
katman          = 4
minToplam       = sum(liste)            #129_977_413
while katman > 0:
    if len(liste) == 0:
        logging.warning(f'{sira}\t İşlem sonlandı.. Sonuç = {minToplam}')
        sira+=1
        logging.warning(f'{sira}\t Süre = {saniyeCevir(time.time()-ilkZaman)}')
        sira+=1
        break

    logging.warning(f'{sira}\t katman {katman} taranıyor..')
    sira+=1
    liste           = liste[:katman]   
    denenen = liste.pop()+2             
    logging.warning(f'{sira}\t {denenen} sayısı deneniyor..')
    sira+=1
     
    denemeSayisi += 1
    yList,sira = bese_tamamla(liste,sira,denenen,sonEleman)
    if len(yList) < 5: #675 ile başlanır 129... a kadar 5li bulamassa diğer katmana geçilir.
        #katman -= 1
        continue
    #5'li bulduysak...
    if sum(yList) < minToplam:
        liste = yList
        minToplam = sum(liste)
        sonEleman = liste[-1]
        logging.warning(f'\n\n{sira}\t daha küçük liste toplami bulundu --> {sum(liste)}.\n\n')
        sira+=1
        katman = 4  #katman başa döner
        continue
    elif sum(yList) > minToplam:  # minToplamdan büyükse sayı değiştir tekrardene
        liste = yList
        logging.warning(f'{sira}\t daha büyük liste toplami bulundu --> {sum(liste)}.')
        sira+=1
        #denenen +=2
        #yList,sira = bese_tamamla(liste,sira,denenen,sonEleman)
        #katman -= 1 aynı katmanda kalır böylece denenen 2 daha arttırılır
        continue

logging.warning(f'{sira}\t katman {katman} taranıyor..')
sira+=1
logging.warning(f'{sira}\t Süre = {saniyeCevir(time.time()-ilkZaman)}')

sira+=1
print(minToplam)



#print(saniyeCevir(time.time()-ilkZaman))
