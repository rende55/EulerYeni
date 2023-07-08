import copy


def kokListe(n):                            #KÖK LİSTE TOPLAMI n EDEN İKİLİ LİSTELER
    mL = list()
    for kok in range(n-1,0,-1):
        kalan = n-kok
        for i in range(1,kalan+1):
            if i <= kok:
                mL.append([kok,i])
    return mL




def anaFonksiyon(m):
    listeBaz = kokListe(m)
    maksToplam      = m
    maksDerinlik    = m
    derinlik = 2
    newList = list()
    sayac = 0
    #listeEk = list()
    #print(listeBaz)
    while derinlik < maksDerinlik:
        
        #print(f'{derinlik+1}. DERİNLİĞE GEÇİLİYOR')
        for altListe in listeBaz:
            sayac+=1
            #print(sayac)
            #print(altListe)
            kalan = maksToplam - sum(altListe)
            if kalan == 1: # alt liste + i toplamından byükse ve  alt listenin son elemanı i den büyük eşitse 
                altListe.append(kalan)
            if kalan > 1:
                listem = copy.deepcopy(altListe)
                #listem = altListe
                listeBaz.remove(altListe)
                newList = [listem+[i] for i in range(1,kalan+1) if i+sum(listem)<=maksToplam and listem[-1]>= i]
                #print(newList)
                for i in newList:
                    listeBaz.append(i)




        #print(listeBaz)
        derinlik += 1

    
    return sorted(listeBaz,reverse=True)


t1 = anaFonksiyon(100)
print(len(t1))