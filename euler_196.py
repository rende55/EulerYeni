import time
import logging


logging.basicConfig(filename="TEST_196_PrimeTriplet.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

'''

Build a triangle from all positive integers in the following way:

1
2  3
4  5  6
7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37.

You are given that S(10000)=950007619.

Find  S(5.678.027) + S(7.208.785).

def asal_komsu_sayisi(anaListe,komsular,sayi):
    sayac = 0
    tripletler = []
    for index,liste in enumerate(anaListe):
        komsuX = komsular[index]
        for komsu in komsuX:
            if asal_mi(liste[komsu]):
                tripletler.append(liste[komsu])
                #print(f'{liste[komsu]} asaldır')
                sayac += 1 
    #print(f'{sayi} sayisina komsu toplam asal sayısı = {sayac}')
    return sayac,tripletler



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


def baslangic_sayisi(n):
    bosluk = 0
    for i in range(1,n):
        bosluk += i
    return(n**2 - (bosluk+n-1))


def liste_yap(n):
    liste = []
    for nx in range((n-2),(n+3)):
        sayi = nx
        baslangic = baslangic_sayisi(nx)
        l1 = list()
        for i in range (baslangic,baslangic+sayi):
            l1.append(i)
        liste.append(l1)
    return liste


def komsulari_bul(koordinat,maxLength): # koordinat ve liste uzunluğu
    (a,b) = koordinat
    komsular = []
    #listelerin son elemanları -------------
    sonAra = maxLength - 1  
    sonUst = maxLength - 2
    sonAlt = maxLength
    #---------------------------------------
    for x in range (-1,2):
        if a+x < 0:
            continue
        for y in range (-1,2):
            if b+y < 0:
                continue
            if x == -1:                 #ust listedeyiz
                if b+y > sonUst:
                    break
            elif x == 0:
                if b+y > sonAra:
                    break
            else:
                if b+y > sonAlt:
                    break
            if (a+x,b+y) != koordinat:
                komsular.append((a+x,b+y))
    return komsular


def sayiyacevir(koordinat,anaListe):
    (x,y) = koordinat
    return anaListe[x][y]


def birinci_komsuda_bak(koord,sira,anaListe):
    komsularBirinciDerece = komsular(koord,sira)
    #logging.warning(f'{koord} koordinatının komşu sayısı =  {len(komsularBirinciDerece)}')
    say = 0
    for komsu in komsularBirinciDerece:
        komsuSayi = sayiyacevir(komsu,anaListe)
        #logging.warning(f'{koord} koordinatının komşusu =  {komsuSayi}')
        if asal_mi(komsuSayi):
            say+=1
        if say == 2:
            return True
    return False


def uclu_yap(koord,sira):
    komsularBirinciDerece = komsular(koord, sira)
    ucluKoordinatlar = list()
    for komsukoordinat in komsularBirinciDerece:
        (x,y) = komsukoordinat
        if x < koord[0]:
            altKomsular = komsular(komsukoordinat,sira-1)
            for altKomsu in altKomsular:
                uc = (altKomsu,komsukoordinat,koord)
                ucluKoordinatlar.append(uc)
        if x == koord[0]:
            altKomsular = komsular(komsukoordinat,sira)
            for altKomsu in altKomsular:
                uc = (altKomsu,komsukoordinat,koord)
                ucluKoordinatlar.append(uc)
        if x > koord[0]:
            altKomsular = komsular(komsukoordinat,sira+1)
            for altKomsu in altKomsular:
                uc = (altKomsu,komsukoordinat,koord)
                ucluKoordinatlar.append(uc)
    return ucluKoordinatlar


def ucluleri_sayilara_cevir(koorListem,anaListem):
    listeyeni = list()
    yeni = list()
    for li in koorListem:
        l1 = list()
        for (x,y) in li:
            l1.append(anaListem[x][y])
        listeyeni.append(l1)
    for lx in listeyeni:
        lx = list(set(lx))
        yeni.append(lx)
    #print(f'\n\n {listeyeni}')
    a = []
    for lx in yeni:
        if len(lx) == 3:
           #print(f'{lx} boyutu 3 tür. ekleniyor')
            a.append(lx)     
    return a    


def uclu_asal_mi(uclu):
    for i in uclu:
        if asal_mi(i) == False:
            return False
        else:
            continue
    return True


def komsular(koordinat, listeuzunlugu):         #sirayla, 9
    (x,y) = koordinat
    ustListeSonElemany = listeuzunlugu - 2      # 7
    araListeSonElemany = listeuzunlugu - 1      # 8
    altListeSonElemany = listeuzunlugu          # 9
    komsular = list()
    for a in range(-1,2):
        if a+x < 0 :
            continue                             # x = 0 ise -1 olacak sonuçları atla
        for b in range(-1,2):
            if b+y < 0 :
                continue
            if x > x+a:
                if b+y > ustListeSonElemany :
                    break
            if x == x+a:    
                if b+y > araListeSonElemany :
                    break
            if x < x+a:    
                if b+y > altListeSonElemany :
                    break
            k = (a+x, b+y)
            if k != (koordinat):
                komsular.append(k)
    #print(f'{listeuzunlugu}. sıradaki {koordinat} koordinatının komşuları = {komsular}')
    return komsular


def main(sira):
    ti1 = time.time()
    #logging.warning(f'{sira}. SIRADAKİ SAYILAR OLUŞTURULUYOR \n')   
    mainList = liste_yap(sira)              #  9.998 9.999 10.000 10.001 10.002 sayılı listeler alınıyor..
  
    bakilacak = mainList[2]                 # ortadaki liste bizim döngüye alacağımız ana liste olacak
    toplam = 0
    for indis, sayi in enumerate(bakilacak):
        if asal_mi(sayi) == False:
            continue
        indisxy = (2, indis)
        if birinci_komsuda_bak(indisxy,sayi,mainList):
            a = saniyeCevir(time.time()-ti1)
            toplam += sayi
            logging.warning(f'\n ----------------------- \n {indisxy} KOORDİNATININ İKİ KOMŞUSU ASALDIR -- {sayi} TOPLAMA EKLENİYOR... \nToplam = {toplam}\n süre = {a} \n -----------------------\n')
            continue
        
        
        
        
        tum = uclu_yap(indisxy,len(bakilacak))
        #logging.warning(f'ÜÇLÜ KOORDİNATLAR -- {tum}')
        tumu = ucluleri_sayilara_cevir(tum,mainList)
        #logging.warning(f'{indisxy} için ÜÇLÜ SAYILAR TOPLAMI -- {len(tumu)} \n ÜÇLÜ SAYILAR:')
        for indis, uclu in enumerate(tumu):
            #logging.warning(f'\n{indis+1}. ÜÇLÜ DENENİYOR...')
            if uclu_asal_mi(uclu):
                a = saniyeCevir(time.time()-ti1)
                logging.warning(f'\n ----------------------- \n {uclu} ÜÇLÜSÜ TAMAMI ASALDIR -- {sayi} TOPLAMA EKLENİYOR...\nToplam = {toplam} \n süre = {a} \n -----------------------\n')
                toplam += sayi
                break
            #else:
                #logging.warning(f'\n XXXXXXXXX \n {uclu} ÜÇLÜSÜ TAMAMI ASAL DEĞİLDİR..\n XXXXXXXXX \n')

    logging.warning(f'toplam sayı = {toplam}\nsüre = {saniyeCevir(time.time()-ti1)}') 
    return toplam




#print(main(10))

a = main(5678027)
print(a)
b = main(7208785)
print(b)
print(a+b)
logging.warning(f'S(5678027) + S(7208785) = {a+b} ')