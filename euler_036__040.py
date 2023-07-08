import time


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


#euler36()
#euler37()
#euler38()
#euler39()
#euler40()