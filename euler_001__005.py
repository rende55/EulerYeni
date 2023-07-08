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


#---------------------------------------#
#euler1()
#euler2()
#euler3(600851475143)
#euler4()
#euler5()
