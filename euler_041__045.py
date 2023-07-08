import time
def euler41():

    #listem = [i for i in range(1,10)]

    #print(listem)
    #print(f'\t {len(listem)} basamaklı sayılar deneniyor....')
      
    def basamak_sayisini_bul(sayi):
        basamakSayisi = 0
        if sayi / 10 < 1 :
            basamakSayisi = 1
            return basamakSayisi

        while sayi > 1:
            basamakSayisi += 1
            sayi = sayi / 10
        return basamakSayisi
    '''
    print(basamak_sayisini_bul(19765243))
    print('BİTTİ')    
    '''
    def pandijital_mi(sayi):
        for i in range(1,basamak_sayisini_bul(sayi)+1):       # 1 ile basamak sayısı arası 4 bs -> 1,2,3,4
            if str(sayi).count(str(i)) == 1:
                continue
            else:
                return False
        return True

    def asal_mi(sayi):
        if sayi == 0 or sayi == 1:
            return False
        karekok = int(round(sayi**0.5))
        #print(karekok)
        for a in range(2,karekok+1):
            if sayi % a == 0:
                return False
            else:
                continue
        else:
            return True
    


    a = 0
    t1 = time.time()
    for i in range(987654321,10,-2):
        a += 1
        #if a % 10000 == 0:
        #    print(f'{a}. sayı deneniyor...')
        #    pass
        if pandijital_mi(i):
            #print(f'\n pandijital bulundu: \t\t\t {i} .',end='',flush=False)
            if asal_mi(i):
                #print('')
                #print('\t\t\t asal da bulundu....\n')
                print(i)
                break
    t2 = time.time()
    print((t2 - t1)//60, 'dakika sürdü')
    '''
    for i in range(987654322,1,-1):
        a += 1
        print(f'{a}. sayı deneniyor...')
        if asal_mi(i):
            print(f'\n asal bulundu \n\n \t\t\t {i}')
            if pandijital_mi(i):
                print('')
                print('\t\t\t bulundu....\n')
                print(i)
                break
    '''

def euler42():
    '''
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    By converting each letter in a word to a number corresponding to its alphabetical position
    and adding these values we form a word value. For example, the word value 
    for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
    Using words.txt (right click and 'Save Link/Target As...'), 
    a 16K text file containing nearly two-thousand common English words, 
    how many are triangle words?
    
    
    
    
    
    
    '''
    harfler = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ucgenDeger = [int(n*(n+1)/2) for n in range(1,1000)]
    #print(ucgenDeger)

    
    lines = list()
    with open('p042_sozcukler.txt') as file:
        for line in file:
            line = line.replace('"','')
            line = line.split(',')
            lines.append(line)
        kelimeler = lines[0]
    def kelime_degeri(kelime):
        deg = 0
        for harf in kelime:

            hd = harfler.index(harf) + 1
            #print(f'harf: {harf}, değeri: {hd}.. ')
            deg += hd
        return deg

    sayac = 0
    for kelime in kelimeler:
        if kelime_degeri(kelime) in ucgenDeger:
            sayac+=1

    print(sayac)

def euler43():
    '''
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
    but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    
    '''
    def pandijital_mi(sayi):
        for i in range(10):       # 1 ile basamak sayısı arası 4 bs -> 1,2,3,4
            if str(sayi).count(str(i)) == 1:
                continue
            else:
                return False
        return True
    
    def ikinci_sart(sayi):
        sayiStr = str(sayi)
        a,b = 0,3
        listeB = [2,3,5,7,11,13,17]

        for bolen in listeB:
            a = a+1
            b = b+1
            sayi = int(sayiStr[a:b])
            if sayi%bolen != 0:
                return False
        return True    
    toplam = 0
    print(pandijital_mi(1406357289))
    st = 1406357289
    print(str(st)[5])
    for i in range(1023456789,9876543211):
        if int(str(i)[5]) % 5 != 0:
            continue
        if int(str(i)[3]) % 2 != 0:
            continue
        if pandijital_mi(i):
            #print(f'{i} sayısı pandijitaldir. ikinci şart aranıyor...')
            if ikinci_sart(i):
                toplam +=i
                print(f'\tiki şart da sağlandı. {i} sayısı toplama ekleniyor... toplam = {toplam}')
                    
    print(f'SON TOPLAM = {toplam}')

def euler44():
    '''
    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
    '''
    def pentagonal(n):
        return int(n*(3*n - 1)/2)
    
    print(pentagonal(2167)-pentagonal(1020))

    pList = []
    for i in range(10000):
        pList.append(pentagonal(i))
    #print(pList)

    for a in pList:
       
        if a == 0:
            continue
        for b in pList:
            if b == 0 or a>=b:
                continue
            if a+b in pList:
                if b-a in pList:
                    print(f'P({pList.index(a)}) = {a}, P({pList.index(b)}) = {b}, P({pList.index(a+b)}) = {a+b}')
                    break
        else:
            continue
        break  

    else:
        print('BULUNAMADI..')
   
#euler41()
#euler42()
#euler43()
euler44()


    
