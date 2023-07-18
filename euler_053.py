
'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 
.

In general, 
 
, where 
, 
, and 
.

It is not until 
, that a value exceeds one-million: 
.

How many, not necessarily distinct, values of 
 for 
, are greater than one-million?
'''


def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    sonuc = 1
    for i in range(1,n+1):
        sonuc = sonuc*i
    return sonuc

def kombinasyon(n,r):
    sonuc = int(faktoriyel(n)/(faktoriyel(r)*faktoriyel(n-r)))

    return sonuc

sayac = 0
for sayi in range(2,101):
    for i in range(1,sayi+1):
        sonuc = kombinasyon(sayi,i)
        if sonuc >= 1_000_000:
            sayac+=1
            print(f'1 milyondan büyük {sayac}. sonuç bulundu C({sayi},{i}) = {sonuc}')
            
print(sayac)


