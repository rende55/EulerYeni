import time

def euler31():
    '''
    In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
    '''
 
    
    bozukluklar = [1,2,5,10,20,50,100,200]
    eris = 200
    for deger in bozukluklar:
        globals()['a_'+str(deger)] = 200//deger  # püf
    sayac = 0
    def toplam(d1=0,d2=0,d5=0,d10=0,d20=0,d50=0,d100=0,d200=0):
        return d1*1+d2*2+d5*5+d10*10+d20*20+d50*50+d100*100+d200*200	
    t1 = time.time()
    for d1 in range(a_1+1):
        fr = toplam(d1)
        if fr > eris:
            break

        for d2 in range(a_2+1):
            fr = toplam(d1,d2)
            if fr > eris:
                break

            for d5 in range(a_5+1):
                fr = toplam(d1,d2,d5)
                if fr > eris:
                    break

                for d10 in range(a_10+1):
                    fr = toplam(d1,d2,d5,d10)
                    if fr > eris:
                        break

                    for d20 in range(a_20+1):
                        fr = toplam(d1,d2,d5,d10,d20)
                        if fr > eris:
                            break

                        for d50 in range(a_50+1):
                            fr = toplam(d1,d2,d5,d10,d20,d50)
                            if fr > eris:
                                break


                            for d100 in range(a_100+1):
                                fr = toplam(d1,d2,d5,d10,d20,d50,d100)
                                if fr > eris:
                                    break

                                for d200 in range(a_200+1):
                                    fr = toplam(d1,d2,d5,d10,d20,d50,d100,d200)
                                    if fr > eris:
                                        break
                                    if fr == eris:
                                        sayac += 1	
                                        #print(sayac,'\t\t', d1,d2,d5,d10,d20,d50,d100,d200,sep='\t')
    t2 = time.time()									
    print(sayac, (t2-t1), sep='\t\n')
def euler32():

    '''

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

    -- pandijital sayılar n basamaklı bir sayı  1 den n'e kadar tüm rakamları kullanıyor ise pandijital sayı demektir. 15234 -> 5 basamaklı pandijital sayıdır.
    -- 7254 sayısı sıradışıdır. 39 x 186 = 7254, çarpanlar ve çarpım 1 den 9 a pandijitaldir.
    -- bu şekilde çarpanlarıyla birlikte 1 den 9'a pandijital olan tüm çarpımların toplamı nedir. 

        * iki basamaklı iki sayı çarpımı max 4 basamaklı sayı olur -- toplam basamak 9 olacak.
            * 
                1b x 3b = 3 - 4     -
                1b x 4b = 4 - 5     + 1,4,4 olur
                2b x 2b = 3 - 4     -
                  2b x 3b = 4 - 5 	+ 2,3,4 olur
                  2b x 4b = 5 - 6 	- 

    '''
    def tekli_mi(sayi):
        sayininRuhu = str(sayi)
        basamaksayisi = len(sayininRuhu)
        for s in sayininRuhu:
            if sayininRuhu.count(s) > 1 :
                return False
        return True

    def eslesebilir_mi(sa1,sa2):
        ruh1 = str(sa1)
        ruh2 = str(sa2)
        if '0' in ruh1 or '0' in ruh2:
            return False

        for s in ruh1:
            if s in ruh2:
                return False
        return True
    pandijitalCarpimlar = set()
    carpan1_1 = [a for a in range(1,10)]
    carpan1_2 = [a for a in range(1234,9877) if tekli_mi(a)]
    carpim	  = [a for a in range(1234,9877) if tekli_mi(a)]

    carpan2_1 = [a for a in range(12,99) if tekli_mi(a)]
    carpan2_2 = [a for a in range(123,988) if tekli_mi(a)]


    for c1 in carpan1_1:
        for c2 in carpan1_2:
            if eslesebilir_mi(c1,c2):
                if c1*c2 in carpim:
                    if eslesebilir_mi(c1,c1*c2) and eslesebilir_mi(c2,c1*c2):
                        print(c1,' x ',c2, ' = ', c1*c2)
                        pandijitalCarpimlar.add(c1*c2)

    for c1 in carpan2_1:
        for c2 in carpan2_2:
            if eslesebilir_mi(c1,c2):
                if c1*c2 in carpim:
                    if eslesebilir_mi(c1,c1*c2) and eslesebilir_mi(c2,c1*c2):
                        print(c1,' x ',c2, ' = ', c1*c2)
                        pandijitalCarpimlar.add(c1*c2)

    print(sum(pandijitalCarpimlar))					
def euler33():
    '''
    49/98 kesri ilginç bir kesirdir, çünkü deneyimsiz bir matematikçi bunu basitleştirmeye 
    çalışırken yanlış bir şekilde 49/98 = 4/8'in 9'ları iptal ederek elde edildiğine inanabilir.

    30/50 = 3/5 gibi kesirleri önemsiz örnekler olarak kabul edeceğiz.

    Değeri birden az olan ve pay ve paydada iki basamak içeren bu tür kesirlerin tam olarak
    dört örneği vardır.

    Bu dört kesrin çarpımı en küçük ortak terimleriyle verilmişse paydanın değerini bulunuz.
        
    '''

    def sadeles(x,y):
        sonuc = x/y
        xs,ys 			=   str(x),str(y)
        x0,x1,y0,y1		=	int(xs[0]) ,int(xs[1]), int(ys[0]), int(ys[1])
        #print(f'1. Sayı {x}, 2. Sayı {y} Bölüm : {sonuc}')
        if x0 == y0 and x1 != 0 and y1 != 0:
            sonuc1 = x1/y1
            if sonuc == sonuc1:
                return True

        if x0 == y1 and x1 != 0 and y0 != 0:
            sonuc2 = x1/y0
            if sonuc == sonuc2:
                return True

        if x1 == y0 and x0 != 0 and y1 != 0:
            sonuc3 = x0/y1
            if sonuc == sonuc3:
                return True	
                
        if x1 == y1 and x0 != 0 and y0 != 0:
            sonuc4 = x0/y0
            if sonuc == sonuc4:
                return True

        return False
    crp1 = 1
    for a in range(10,100):
        for b in range(10,100):
            
            sayiA = str(a)
            sayiB = str(b) 

            if sayiA[1] == '0' and sayiB[1] == '0': 			# birler basamağı 0 sa atlanacak
                continue
            if a/b >= 1:										# bölüm 1'den büyükse atlanacak
                continue
            if sadeles(a,b):
                crp1 = crp1*(b/a)
    print(crp1)
def euler34():
    '''
    145, ilginç bir sayı 1! 4! 5! = 1 24 120 = 145. 
    Rakamlarının faktöriyellerinin toplamına eşit olan tüm sayıların toplamını bulun. 
    Not: 1! = 1 ve 2! = 2, dahil edilmedikleri toplamlar değildir.
    '''
    def ayristir(sayi):
        sonuc = sayi
        sayiRakamlari = list()
        while sonuc > 0:
            a = sonuc%10
            sayiRakamlari.append(a)
            sonuc = sonuc//10
        return sayiRakamlari

    def faktoryel_topla(listem):
        toplam = 0
        for rakam in listem:
            carpim = 1
            for i in range(1,rakam+1):
                carpim *= i
            toplam += carpim
        return toplam
    a = 0
    for s in range(3,100_000):
        
        if faktoryel_topla(ayristir(s)) == s:
            a+=s
    print(a)        
def euler35():
    '''
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
    
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
    '''
    circularSayisi = 0
    def formasyon(asalsayi):
        sayi = str(asalsayi)
        rakamlar = [i for i in sayi]
        rSayisi = len(rakamlar) #3
        degerler = list()
        for a in range(rSayisi):
            deger = ''
            for i in rakamlar: #1,9,7
                #print(type(i))
                deger += i
            degerler.append(int(deger))
            rakamlar.insert(0,rakamlar.pop())
        return degerler
    
    def asal_mi(sayi):
        karekok = int(round(sayi**0.5))
        #print(karekok)
        for a in range(2,karekok+1):
            if sayi % a == 0:
                return False
            else:
                continue
        else:
            return True
    t1 = time.time()
    for i in range(2,1_000_000):
        if asal_mi(i):
            degerlerim = formasyon(i)
            for deger in degerlerim:
                if asal_mi(deger):
                    continue
                else:
                    break
            else:
                print(degerlerim[0], 'circular')
                circularSayisi += 1
    t2 = time.time()
    print('\t Sirküler asal sayısı = ' , circularSayisi)
    print('\t\t İşlem Süresi = ' , t2-t1)
def euler36():
    sayilar = []
    for i in range(1,1_000_000):
        z = str(i)[::-1]
        if str(i) == z:
            a = str(bin(i))[2:]
            b = a[::-1]
        if a == b:
            sayilar.append(i)
            print(i, a)
    print(sum(sayilar))
def euler37():
    '''
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
    and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
    
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    2, 3, 5, and 7 are not considered to be truncatable primes.
    
    '''
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
    def find_digit(number):
        digit = 0
        while number >1:
            digit+=1
            number = number //10
        return digit
    def remove_right_to_left(number):
        rightList = list()       
        while number > 0:
            number = number//10
            if number > 0:
                rightList.append(number)
        return rightList
    def remove_left_to_right(number):
        digit = find_digit(number)
        leftList = list()
        while digit > 1:
            number = number % 10**(digit-1)
            leftList.append(number) 
            digit -=1
        return leftList
    saybakalim = 0
    arananSayi = list()
    a = time.time()
    for sayi in range(10,10_000_000):
        if saybakalim == 11:
            break
        if asal_mi(sayi) == False:
            continue
        else:
            #print('\n', sayi, ' sayisi asal. ikinci aşamaya geçiliyor')
            sagdan = remove_right_to_left(sayi)
            #print(sagdan)
            for s1 in sagdan:
                #print('sağdan say')
                if asal_mi(s1):
                    #print('\t', s1, 'sayisi asal')
                    continue
                else:
                    break
            else:
                #print('sağdan tamamı asal, sola geçiliyor')
                soldan = remove_left_to_right(sayi)
                #print(soldan)
                for s2 in soldan:
                    #print('soldan say')
                    if asal_mi(s2):
                        #print('\t', s2, 'sayisi asal')
                        continue
                    else:
                        break
                else:
                    print(sayi, ' sayisi sağdan ve soldan asal..')
                    arananSayi.append(sayi)
                    saybakalim += 1
    b = time.time()
    print('\n\n')                
    #print(arananSayi) 
    print(sum(arananSayi),(b-a),sep='\t\t') 
              
            

    remove_left_to_right(3797)
    #remove_right_to_left(3797)
def euler38():
    '''
    
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. 
    We will call 192384576 the concatenated product of 192 and (1,2,3)


    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
    which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number 
    that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1? 
    
    
    sayi = int(str(sayi*1) + str(sayi*2) + .... + str(sayi*n))
    kısaltmk için iki basamaklıdan başla 98 - 91 arası
    üç basamaklı 987 - 912 arası
    ya da 9 basamak için en fazla 4 basamaklı bir sayı olur.. 10bine kadar ara


    '''

    def basamak_sayisi(sayi):
        bs = 0
        while sayi > 1:
            bs += 1
            sayi = sayi//10  
        return bs

    def pandijital_mi(sayi):
        for i in range(1,10):
            if str(sayi).count(str(i)) == 1:
                continue
            else:
                return False
        return True
   
    for i in range(8,10_000):
        if i//10**(basamak_sayisi(i)-1) != 9:
            continue
        else:
            sayi = i
            n = 2
            while basamak_sayisi(sayi) < 9:  
                sayi = int(str(sayi)+str(i*n))
                n +=1
            if basamak_sayisi(sayi) == 9: 
                if pandijital_mi(sayi):
                    print(sayi,n-1)
                else:
                    continue
            else:
                continue
    else:
        print('Bulunamadı')                 
def euler39():
    '''
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
    there are exactly three solutions for p = 120.   {20,48,52}, {24,45,51}, {30,40,50}
    For which value of p ≤ 1000, is the number of solutions maximised?
    
    c = (a**2 + b**2)**(1/2)
    belki üçgen kuralıyla sorgulayıp kısalabilir ??
    '''
 

    def ekle_veya_topla(sozluk,anahtar):
        if anahtar in sozluk.keys():
            deger = sozluk[anahtar]
            sozluk[anahtar] = deger+1
        else:
            deger = 1
            sozluk[anahtar] = deger
        return sozluk


    def tam_sayi_mi(sayi):
        if c/int(c) == 1:
            return True
        return False
    pSozlugu = {}
    for a in range(1,1000):
        for b in range(1,1000):
            if a < b:
                continue          
            c = (a**2 + b**2)**(1/2)
            if tam_sayi_mi(c):
                c = int(c)
                p = a+b+c

                    
                if p < 1000:
                    ekle_veya_topla(pSozlugu,p)
    
    anht = 0
    deg = 0
    for key,value in pSozlugu.items():
        if value > deg:
            anht = key
            deg = value
    print(anht, deg)

    #print(pSozlugu)
def euler40():
    '''
    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    
    
    
    '''
    ss = ''
    for i in range(1,10**6):
        ss = ss+str(i)
  

    def sayi(st, sira):
        s = st[sira-1]
        print(s)
        return int(s)

    d1,d10,d100,d1000,d10000,d100_000,d1_000_000 = sayi(ss,1),sayi(ss,10),sayi(ss,10**2),sayi(ss,10**3),sayi(ss,10**4),sayi(ss,10**5),sayi(ss,10**6)
    print(d1,d10,d100,d1000,d10000,d100_000,d1_000_000,sep=' x ',end=' = ')
    print(d1*d10*d100*d1000*d10000*d100_000*d1_000_000)
    '''
    l = len(s)
    s = int(s)
    s = s/10**(l)
    d10 = int(s*(10**10))
    print(d10)
    '''


