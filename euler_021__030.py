import time

def euler21():
	'''
	Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
	If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

	For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

	Evaluate the sum of all the amicable numbers under 10000.	
	'''
	a = dict()
	def toplam_bolen(n):	
		b = []
		for i in range (1,n):
			if n%i == 0:
				b.append(i)
		a[str(n)] = sum(b)
	for i in range (1,10000):
		toplam_bolen(i)
	#print(a, sep='\n')
	c = set()
	for key, value in a.items():
		for k,v in a.items():
			if int(key) == v and int(k) == value and int(key) != value:
				c.add(value)
				#print(f'd({key}) = {value} \t d({k}) = {v}\n\n')
	print(sum(c))
def euler22():
	'''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

	For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

	What is the total of all the name scores in the file?'''
	lines = []
	with open('p022_names.txt') as file:
		for line in file:
			line = line.replace('"','')
			line = line.split(',')
			lines.append(line)
		lines = lines[0]
	lines = sorted(lines)
			
	
	deger_listesi = {
		'A':1,
		'B':2,
		'C':3,
		'D':4,
		'E':5,
		'F':6,
		'G':7,
		'H':8,
		'I':9,
		'J':10,
		'K':11,
		'L':12,
		'M':13,
		'N':14,
		'O':15,
		'P':16,
		'Q':17,
		'R':18,
		'S':19,
		'T':20,
		'U':21,
		'V':22,
		'W':23,
		'X':24,
		'Y':25,
		'Z':26
	}
	def toplam(kelimelistesi,deger_list):
		sonuc = 0
		for sira,kelime in enumerate(kelimelistesi, 1):		
			ara_sonuc = 0
			topla = 0
			for harf in kelime:
				topla = topla + deger_list[harf]
			ara_sonuc = topla * sira
			sonuc += ara_sonuc
		return sonuc
	print(toplam(lines,deger_listesi))
def euler23():	# İŞLEM SÜRESİ 40 SANİYE - 15 sn. revizyon
	import copy
	'''
	A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
	For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

	A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

	As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
	By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
	However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
	
	Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

	--> mükemmel sayı 	: pozitif bölenlerinin toplamı kendisine eşit sayı. örnek 28 == 1+2+3+4+7+14 
	--> dar sayı		: pozitif bölenlerinin toplamı kendisinden küçük sayı.
	--> geniş sayı		: pozitif bölenlerinin toplamı kendisinden büyük sayı.
		--> en küçük geniş sayı : 12 < toplam(1,2,3,4,6)
	--> iki geniş sayının toplamı olarak yazılabilecek en küçük sayı 24. (12+12 mi nedir artık yazmıyor..)
	--> matematiksel analizlere göre, 28123'den büyük bütün sayılar iki geniş sayının toplamı olarak yazılabilir. 
	--> şimdi soru şu : iki geniş sayının toplamı olarak yazılamayacak bütün pozitif tamsayıların toplamı nedir? (WTF!)

	28123'ten büyük bütün sayılar herhangi iki geniş* sayının toplamı ile yazılabilir.
	iki geniş sayının toplanmasıyla bulunamayacak tam sayıların toplamını bul.
	'''
	def genisSayilar(n): 					# çarpan toplamı n den büyükse geniş sayı ...
		#print(f'sayımız {n} hesaplanıyor...') 
		carpantoplami = 0
		for i in range(1,(n//2+1)): 		# en büyük çarpan n/2 den büyük olamaz
			#print(f'carpan sayimiz {i} ....')
			if n % i == 0:
				carpantoplami += i
				#print(f'çarpan toplamı.. {carpantoplami}')
				if carpantoplami > n:
					#print('\n\t\t\t geniş sayı..')
					return True
				else:
					continue
		return False
	genisliste = list()
	t1 = time.time()
	for n in range (12,28124):				# 28123'ten büyük sayıları denemeye gerek yok 
		#y = genisSayilar(n)
		if genisSayilar(n):
			genisliste.append(n)
	t3 = time.time()
	#gl1 = copy.deepcopy(genisliste)
	gLToplam = set()						# toplam aynı olacak olanların birini almak yeterli. o yüzden set
	for a in genisliste:
		for b in genisliste:
			gLToplam.add((a+b))				# geniş iki sayının bütün toplamlarını aldık..
	toplam = 0 
	for i in range(1,28123):				# 28123 e kadar bütün sayıları deniyoruz. gltoplam kümemizde yoksa aradığımız değeri buluyoruz.
		if i not in gLToplam:
			toplam += i

	t2 = time.time()
	print(f'süre1 : {t3-t1} saniye;   \t\t süre2 : {t2-t3} saniye;  \t\t TS : {t2-t1} saniye; \n\n\t\t\t\t SONUÇ = {toplam}')
def euler24():

	'''
	A permutation is an ordered arrangement of objects. 
	For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
	If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
	The lexicographic permutations of 0, 1 and 2 are:
	012   021   102   120   201   210
	What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
	'''
	from itertools import permutations
	listem = list(range(10))
	perm = list(permutations(listem,10))
	print(perm[1_000_000-1])
def euler25():
	'''
	The Fibonacci sequence is defined by the recurrence relation:

	Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
	Hence the first 12 terms will be:

	F1 = 1
	F2 = 1
	F3 = 2
	F4 = 3
	F5 = 5
	F6 = 8
	F7 = 13
	F8 = 21
	F9 = 34
	F10 = 55
	F11 = 89
	F12 = 144
	The 12th term, F12, is the first term to contain three digits.

	What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
	'''
	a = 2
	b = 1
	fib = 0
	index = 3
	while fib // 10**999 == 0:
		fib = a+b
		b = a
		a = fib
		index += 1
	print(fib , index, sep='\t ==>\t')
def euler26():
    '''	
    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    '''
    aradigim_deger = 0 
    aradigim_dongu_sayisi = 0
    for i in range(2, 1000):                                                                                                             
        kalanlar = []
        kalan = (10**len(str(i))) % i                  
        while kalan not in kalanlar:     
            kalanlar.append(kalan)                                           
            if kalan == 0:
                break
            while kalan < i:
                kalan *= 10                                                      
            kalan = kalan % i                                                                        
        while kalanlar[0] != kalan:
            kalanlar.remove(kalanlar[0]) 
        if len(kalanlar) > aradigim_dongu_sayisi:
            aradigim_dongu_sayisi = len(kalanlar)
            aradigim_deger = i
    print (aradigim_deger)
    print (aradigim_dongu_sayisi)
def euler27(): 
    '''
    Euler olağanüstü ikinci dereceden formülü keşfetti: n**2 + n + 41
    Formülün, 0≤n≤39 ardışık tamsayı değerleri için 40 asal üreteceği ortaya çıktı. 
    Bununla birlikte, n = 40, 40**2 + 40 + 41 = 40 (40 + 1) +41, 41 ile bölünebilir 
    ve kesinlikle n = 41, 41**2 + 41 + 41 açıkça 41 ile bölünebilir. 
    
    İnanılmaz formül n**2 − 79n + 1601 keşfedildi , 
    0≤n≤79 ardışık değerleri için 80 asal üretir. 

    Katsayıların çarpımı −79 ve 1601, −126479'dur. 
    Formun ikinci dereceden ele alındığında: n**2 + an + b, 
    burada | a | <1000 ve | b | ≤ 1000 
    burada | n | n'nin modül / mutlak değeridir, 
    ör. | 11 | = 11 ve | −4 | = 4 
    n = 0'dan başlayarak ardışık n değerleri için maksimum asal sayısını üreten ikinci dereceden ifade için a ve b katsayılarının çarpımını bulun.
    
    
    '''	
    def asal_mi(say):
        karekok = int(round(abs(say**0.5)))
        #print(type(karekok))
        for a in range(2,karekok+1):
            if say % a == 0:
                return False
            else:
                continue
        else:
            return True
    
    mx1 = (0,0,0)
    for a in range(-1000,1000):
        for b in range(-1000,1001):
            for n in range(81):
                frm = n**2 + a*n + b
                #print(type(frm))
                if asal_mi(frm):
                    continue
                else: 
                    deg = (a,b,n)
                    if mx1[2] < deg[2]:
                        mx1 = deg
                        print('yeni deger', deg)
                        break
                    else:
                        break
    print('son değer', mx1)
    print(mx1[0]*mx1[1])
def euler28():
    kosegen = 0
    x = 1
    kosegen += x
    for n in range(1,501):
        for i in range(4):
            x += 2*n 
            kosegen += x
    print(kosegen)
def euler29():
    '''
    Consider all integer combinations of a**b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    2**2=4, 2**3=8, 2**4=16, 2**5=32
    3**2=9, 3**3=27, 3**4=81, 3**5=243
    4**2=16, 4**3=64, 4**4=256, 4**5=1024
    5**2=25, 5**3=125, 5**4=625, 5**5=3125
    If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

    '''
    distinctterms = set()
    for a in range (2,101):
        for b in range(2,101):
            distinctterms.add(a**b)
    print(len(distinctterms))
def euler30():
    a = 0
    for i in range(2,10_000_000):
    
        birler 		= i%10
        onlar 		= (i//10)%10
        yuzler 		= (i//100)%10
        binler 		= (i//1000)%10
        ybinler 	= (i//10000)%10
        milyonlar 	= (i//100000)%10
        if (birler**5+onlar**5+yuzler**5+binler**5+ybinler**5+milyonlar**5) == i:
            print(i)
            a = a+i
    print (a)

