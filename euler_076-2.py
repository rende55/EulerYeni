


def kokListe(n):                            #KÖK LİSTE TOPLAMI n EDEN İKİLİ LİSTELER
    mL = list()
    for i in range(1,n):
        k = n-i
        mL.append([k,i])
    return mL


def ayristir(ikiliListem):                  # 2,6
    root = ikiliListem[0]                   # 2 
    tail = ikiliListem[-1]                  # 6 
    newSub = [root]                         # [2]
    while root < tail:                      # kök küçük olduğu kadar uygula... 2<6    #2<4
        kalan = tail - root                 # 4             # kalan = 2
        newSub.append(root)                 # [2,2..]       # [2,2,2...]
        tail = kalan                        # tail = 4      # tail = 2
    if tail > 0:
        newSub.append(tail)
    return newSub

def birlestir(sayi):
    listemiz = list()
    l1 = kokListe(sayi)
    for l_alt in l1:
        t1 = ayristir(l_alt)
        listemiz.append(t1)
    return listemiz

def ayristir_v2(ikiliListem):                  # 2,6
    root = ikiliListem[0]                   # 2 
    tail = ikiliListem[-1]                  # 6 
    newSub = [root]                         # [2]
    while root < tail:                      # kök küçük olduğu kadar uygula... 2<6    #2<4
        kalan = tail - root                 # 4             # kalan = 2
        newSub.append(root)                 # [2,2..]       # [2,2,2...]
        tail = kalan                        # tail = 4      # tail = 2
    if tail > 0:
        newSub.append(tail)
    return newSub



def isle(sayi):
    yeniListe = list()
    anaListe = birlestir(sayi)
    for altListe in anaListe:
        yeniListe.append(altListe)
        altUzunluk = len(altListe)
        kokSayi = altListe[0]
        if altListe[1] == 1:
            continue
        if altUzunluk == 2: #burada operasyon olacak
            kokListe = birlestir(altListe[1])
            for liste2 in kokListe:
                adding = [kokSayi]+liste2
                yeniListe.append(adding)
    return yeniListe


print(birlestir(9))
print('-'*188)
a = isle(100)

for i in a:
    print(i)