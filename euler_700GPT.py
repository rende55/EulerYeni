
import numpy as np
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
from kullanislimodullerim import *


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a                    # çarpan, kalan bulunur ---> b = a.q + r
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

sabita      = 1_504_170_715_041_707
modTabania  = 4_503_599_627_370_517
inv         = 3_451_657_199_285_664
donguS      =       924_571_768_317
#print(list(asalcarpanlar(donguS)))
#print(inv%donguS)
#x1 = sabita*donguS
#son = ((x1+2299)%modTabania)
#print(son)
f = 2021
#print(asal_mi(f))
#print(list(asalcarpanlar(f)))


coinler = '''1504170715041707
8912517754604
2044785486369
1311409677241
578033868113
422691927098
267349986083
112008045068
68674149121
25340253174
7346610401
4046188430
745766459
428410324
111054189
15806432
15397267
14988102
14578937
14169772
13760607
13351442
12942277
12533112
12123947
11714782
11305617
10896452
10487287
10078122
9668957
9259792
8850627
8441462
8032297
7623132
7213967
6804802
6395637
5986472
5577307
5168142
4758977
4349812
3940647
3531482
3122317
2713152
2303987
1894822
1485657
1076492
667327
258162
107159
63315
19471
14569
9667
4765
4628
4491
4354
4217
4080
3943
3806
3669
3532
3395
3258
3121
2984
2847
2710
2573
2436
2299
2162
2025
1888
1751
1614
1477
1340
1203
1066
929
792
655
518
381
244
107
1'''
1517926517777406

listeCoin = [int(x) for x in coinler.split('\n')]


print(len(listeCoin),sum(listeCoin))



yorumlar = '''
logging.basicConfig(filename="700_EulerCoin.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)



dg      = 1_504_170_715_041_707
modS    = 4_503_599_627_370_517

#print(asalcarpanlar(modS))


ts = 4491   #testtendolai degisiyor..
#print(euklid_bolme(modS,dg))
limit = dg*modS
for i in range(3_100_000_000_000,modS):
    snc = (dg*i % modS)
    if snc == 0:
        break
    if i % 1_000_000_000 == 0 :
        print(i, saniyeCevir(time.time() - tt))

    if snc < ts:
        eulerCoins.append(snc)
        print('\n-----------------------------------------------\n')
        logging.warning(f'{i}, {snc}')
        print('\n-----------------------------------------------\n')
        ts = snc


for t in range(modS-1,3_090_000_000_000,-1):
    c = (dg * t % modS)
    if c < ts:
        print(c,t)
        break

        
    ilkSayi      = 1_504_170_715_041_707
    modTabani    = 4_503_599_627_370_517
    carpan = 1
    toplam = 1_504_170_715_041_707              # ilk elemanı doğrudan alıyoruz.
    enKucukCoin = (ilkSayi*carpan)%modTabani
    kalaniBuluncak = ilkSayi*carpan
    while enKucukCoin > 0:                      # mod sonusu sıfır olana kadar sürdür
 
        carpan+=1
        kalan = (ilkSayi*carpan)% modTabani
        if kalan < enKucukCoin:
            print(f'Yeni Coin üretildi.;{kalan};{saniyeCevir(time.time()-t2)};{carpan}')
            #print(f'{ilkSayi},{carpan},{modTabani},{kalan},')
           
            toplam += kalan
            enKucukCoin = kalan
            #modTabani=ilkSayi
            #ilkSayi = kalan
        if carpan >= modTabani:
            break
        if kalan == ilkSayi:
            print(f'{ilkSayi},{carpan},döngüye girdi periyot sonu')
            break
    return toplam



    ilkSayi      = 1_504_170_715_041_707
    modTabani    = 4_503_599_627_370_517
    carpan = 1
    toplam = 1_504_170_715_041_707              # ilk elemanı doğrudan alıyoruz.
    enKucukCoin = (ilkSayi*carpan)%modTabani
    kalaniBuluncak = ilkSayi*carpan
    while enKucukCoin > 0:                      # mod sonusu sıfır olana kadar sürdür
 
        carpan+=1
        kalan = (ilkSayi*carpan)% modTabani
        if kalan < enKucukCoin:
            print(f'Yeni Coin üretildi.;{kalan};{saniyeCevir(time.time()-t2)};{carpan}')
            #print(f'{ilkSayi},{carpan},{modTabani},{kalan},')
           
            toplam += kalan
            enKucukCoin = kalan
            #modTabani=ilkSayi
            #ilkSayi = kalan
        if carpan >= modTabani:
            break
        if kalan == ilkSayi:
            print(f'{ilkSayi},{carpan},döngüye girdi periyot sonu')
            break
    return toplam

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Büyük sayıyı girin
#number = 4503599627370517
ilks = 1504170715041707
#print(asal_mi(number))
#print(asal_mi(ilks))
# Asal çarpanları bul
#factors = prime_factors(ilks)

# Asal çarpanları yazdır
#print("Asal Çarpanlar:", factors)

a = 17
b = 1249
c = 12043
d = 5882353
#n = 1
modTabani = 4503599627370517
s = a*b*c*d
toplam = 0
t2 = time.time()
for n in range(1,modTabani):
    sonuc = a*b*c*((d*n)%modTabani)
    sonucx = sonuc%modTabani
    if sonucx < s :
        print('Yeni coin bulundu...,', sonucx,',', saniyeCevir(time.time()-t2))
        toplam+=sonucx
        s = sonucx
    if sonucx in [0,1]:
        break   
else:
    print (toplam)

'''