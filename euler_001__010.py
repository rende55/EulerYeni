import time
def euler1():
	t = 0
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			t = i + t
		else:
			next
	else:
		print(t)	
def euler2():
	#4 milyonun altındaki fibonacci dizindeki çift sayıların toplamı
	# 1, 2, 3, 5, 8, 13...
	fibonacci = [1,2]
	fib = 0
	while fib < 4_000_000:
		fib = fibonacci[len(fibonacci)-2] + fibonacci[len(fibonacci)-1]
		if fib < 4_000_000:
			fibonacci.append(fib)
		else:
			continue

	a = 0 
	for fib in fibonacci:
		if fib % 2 == 0:
			a = fib + a
	else:
		print(a)
def euler3(sayi):
	# 13195 asal çarpanları 5, 7, 13 and 29.
	# 600851475143 sayısının en büyük asal çarpanı kaçtır 
	for i in range(2,sayi-1):
		if sayi % i == 0:
			sayi = int(sayi/i)
			if sayi == 1:
				break
			else:
				euler3(sayi)	
		else:
			next
	else:
		print(sayi) #son kalan sayı en büyük asal olmak zorunda..
def euler4():
	# palindromik sayı iki yönden de aynı okunan sayılara denir. 
	# iki basamaklı iki sayının çarpımı ile yapılabilece en büyük pal sayı 9009 = 91 × 99.
	# üç basamaklı iki sayının çarpımı ile yapılabilecek en büyük pal. sayı kaçtır?
	for i in range(999,900,-1):
		for t in range(990,900,-11): #sayılardan 1 tanesi 11 e bölünmek zorunda (analiz yapınca çıkıyor)
			palindroma = str(t*i)
			if len(palindroma) < 6:
				break
			else:
				if palindroma[0]==palindroma[5] and palindroma[1]==palindroma[4] and palindroma[2]==palindroma[3]:
					print("{} x {} = {}".format(t, i, palindroma))
				else:
					continue
def euler5():
	#2520 sayısı 1 den 10'a kadar tüm sayılara kalansız bölüne bilen en küçük sayıdır.
	#1'den 20'ye okek?
	asalcrp = []
	sayilar = [a for a in range(20,1,-1)]
	asal = []
	for ab in range(2,sayilar[0]):            #asalları bul         
		for xy in range(2,ab-1):
			if ab % xy == 0:
				break
			else:
				continue
		else:			
			asal.append(ab)
	def bol(sayilar1,a=0):
		sayilar2 = sayilar1.copy()
		for i, sayi in enumerate(sayilar2):
			if sayi % asal[a] == 0:
				sayilar2[i] = int(sayi/asal[a])			
			else:
				continue
		else:		
			if len(set(sayilar2)) != 1:
				if  sayilar1 == sayilar2:
					if a < len(asal)-1:
						a += 1
						bol(sayilar2,a)		
				else:				
					asalcrp.append(asal[a])
					bol(sayilar2,a) #hata: son asal sayı için işlem yapılıyor ancak listeye eklenmiyor
	bol(sayilar)
	c = 1
	for i in asalcrp:
		c= i*c
	print(c*19) 
def euler6(sayi):
	#ilk on sayının kare toplamı,
	#1^2 + 2^2 + ... + 10^2 = 385
	#ilk on sayının toplamının karesi,
	#(1 + 2 + ... + 10)^2 = 552 = 3025
	#arasındaki fark 3025 − 385 = 2640.
	#ilk yüzde ?.
	t = 0
	u = 0
	for say in range(1,sayi+1):
		t = t + say **2
		u = u + say
	print(u**2-t)
def euler7(sira):
	#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	#What is the 10 001st prime number?
	asallar = []
	for ab in range(2,1000000):                     
		for xy in range(2,ab-1):
			if ab % xy == 0:
				break
			else:
				continue
		else:
			if len(asallar) < sira:
				asallar.append(ab)
			else:
				break
	print(asallar[-1])			
def euler8(): 
	#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
	sayi = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	say = str(sayi)
	alt_kume = set()
	altc=[]
	for a in range(987):
		if '0' not in say[a:a+13]: # 0 olduğunda çarpım 0 olacağı için eklenmedi
			alt_kume.add(say[a:a+13])
		else:
			continue
	else:
		c=1
		alt_kume = sorted(alt_kume,reverse=True)
 		
		for i,alt in enumerate(alt_kume):
			for a in alt:
				c = c*int(a)
			else:
				altc.append([c,alt_kume[i]])
				c = 1
		else:
			altc = sorted(altc,reverse=True)
			print(altc[0])			
def euler9():
	'''
	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
	a**2 + b**2 = c**2
	For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.	
	'''
	for c in range(2,900):
		for b in range(2,500):
			for a in range(2,500):
				if ((a**2) + (b**2)) == c**2 :
					if a+b+c == 1000:
						print(a,b,c, a*b*c)
					else:
						continue
				else:
					continue	
def euler10(): #18 dakika 39 sn surdu ---- kısaltıldı 22 sn
	'''
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.'''
	t1 = time.time()
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
	toplam = 0		
	for i in range(2_000_000,2,-1):
		if asal_mi(i):
			#print(i)
			toplam = toplam+i
	print(toplam)

	t2 = time.time()
	
	print(t2-t1)

