
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

# -------------------------------------------------------#

def komsu_listesi(bas,bit,sra):
    listeler = dict()
    for i in range(bas,bit+1):
        if asal_mi(i) == False:
            continue
        #print(i,baslangic)
        liste = list()
        listeust = [a+(i-sra) for a in range(3)]
        listealt = [b+(i+sra) for b in range(-1,2)]
        if i == bas:
            listeust = listeust[1:]
            listealt = listealt[1:]
        if i == bit:
            listeust.pop()
            listeust.pop()
        if i == bit-1:
            listeust.pop()
        liste = listeust+listealt
        listeler[str(i)] = liste
        #print(listeler)
    print(saniyeCevir(time.process_time()))
    
    return listeler

def toplami_bulak(sira):
    baslangic = int((sira*sira)-(((sira)*(sira+1))/2)+1)
    bitis     = baslangic+sira-1
    list1 = komsu_listesi(baslangic,bitis,sira)
    return list1

l2 = toplami_bulak(7_208_785)

#l1 = toplami_bulak(10_000)


def toplam(sozluk):
    toplam = 0
    for key,value in sozluk.items():
        say = 0
        for i in value:
            if asal_mi(i):
                say +=1 
            if say == 2:
                toplam = toplam+int(key)
                print(saniyeCevir(time.process_time()))
                print(toplam)
                print('---\n')
                break
    return toplam


print(toplam(l2))


#---------------------------------------------------------------------------------------

#print('ROOT LIST',rootList(7))


def ayristir(listem):                   #2,6
    root = listem[0]                    # 2 ise
    tail = listem[-1]                   # 6 
    newSub = [root]                     # [2,..]
    while root < tail: # kök küçük olduğu kadar uygula... 2<6    #2<4
        kalan = tail - root             # 4             # kalan = 2
        newSub.append(root)             # [2,2..]       # [2,2,2...]
        tail = kalan                    # tail = 4      # tail = 2
    if tail > 0:
        newSub.append(tail)
    return newSub

#print('AYRISTIR',ayristir(rootList(7)[3]))


def ayristirilmis_kok(n):
    newList = list()
    rootListe = rootList(n)
    for subList in rootListe:
        if subList[0]>=subList[1]:
            newList.append(subList)
            continue
        else:
            subListNew = ayristir(subList)
            newList.append(subListNew)
    return newList

#print('AYRISTIRILMIŞ KÖK',ayristirilmis_kok(7))


def sayi_hesapla(n,count=0):
    listOfList = ayristirilmis_kok(n)
    kalanListe = listOfList
    count+=len(kalanListe)
    kalanListe = []
    for l2 in listOfList:

        if l2[1] == 1:
            continue
        else:

            kalanListe.append(l2)
    #print(kalanListe)
    return count

#print('SAYI HESAPLA',sayi_hesapla(7))

def count_roots(n,c = 0):

    for i in range(1,n):
        c += 1
        if i < n-i:
            count_roots((n-i),c)
        

    return c

print(count_roots(5))