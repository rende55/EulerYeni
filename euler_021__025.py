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

#euler21()
#euler22()
euler23()
#euler24()
#euler25()
