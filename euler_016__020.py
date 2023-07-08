import time

def euler16():
	'''
	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 2^1000
	'''
	def toplami(sayi,ust,toplam=0):
		ax = sayi**ust
		while ax < 10:
			toplam += (ax%10)
			ax = ax//10
		return(toplam)
	 
	print(toplami(2,64))
def euler17(): 
	'''
	If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


	NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
	The use of "and" when writing out numbers is in compliance with British usage.

	'''

	sayilar = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
	'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	ikincibas = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	basamakadi = ['thousand','hundredand']

	def cevir(sayi):
		birler = sayi%10
		onlar = (sayi//10)%10
		yuzler = (sayi//100)%10
		binler = (sayi//1000)%10
		ilkyirmi = sayi%100
		basamaklar = [binler,yuzler,onlar,birler]
		sayioku = ''
		
		for indis, basamak in enumerate(basamaklar):
			if basamak == 0:
				pass
			else:
				if indis < 2:
					sayioku = sayioku+sayilar[basamak]+basamakadi[indis]
					if ilkyirmi == 0 and sayi != 1000:
						return sayioku[:-3]
				else:
					if ilkyirmi > 19:
						if birler == 0:
							sayioku = sayioku+ikincibas[basamak-2]
							break
						else:
							sayioku = sayioku+ikincibas[basamak-2]+sayilar[birler]
							break
					else:
						sayioku = sayioku+sayilar[ilkyirmi]
						break
		return sayioku

	toplam = 0            
	for i in range(1,1001):
		a = cevir(i)
		le = len(a)
		toplam += le
	print(toplam)
def euler18():
	import copy
	lines = []
	with open("p067_triangle.txt") as file: #burada diğer üçgeni alıyoruz.
		for line in file: 
			#line = line.strip() #or some other preprocessing
			line = line.split()
			lines.append(line) 
	
	for line in lines:
		for i in range(0, len(line)): 
			line[i] = int(line[i])
	ucgen3 = lines

	ucgen2 = [
	[75],
	[95, 64],
	[17, 47, 82],
	[18, 35, 87, 10],
	[20, 4, 82, 47, 65],
	[19, 1, 23, 75, 3, 34],
	[88, 2, 77, 73, 7, 63, 67],
	[99, 65, 4, 28, 6, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

	ucgen1 = [
	[3],
	[7, 4],
	[2, 4, 6],
	[8, 5, 9, 3]]

	def max_toplam(ucgen):
		yol_uzunlugu = len(ucgen)
		yol_sayisi = len(ucgen[-1])
		seviye = len(ucgen)-1
		yollar  = [[] for i in range(len(ucgen[-1]))] # tek hamlede doğru yaptık ya la
		for ax in range(len(ucgen[-1])):
			yollar[ax].append(ucgen[-1][ax])
		print(f'toplam {yol_uzunlugu} katman bulunmaktadır.\n')
		yeniyollar = []
		while seviye > 0:    
			yeniyollar = []
			gecici_liste = []
			print(f'---------------------------------------------------------------\n\t{seviye}. katman inceleniyor...\n')
			#print(yollar)
			altliste = ucgen[seviye-1]
			for indeks, deger in enumerate(altliste):
				print(f'\n\t değer : {deger}, sıra: {indeks}.. \nEşleşme {indeks} ve {indeks+1} ile olabilir...')   
				if sum(yollar[indeks]) > sum(yollar[indeks+1]):
					print (f"birinci yol daha büyük,  {deger}, {yollar[indeks]}'e aktarılıyor...")
					gecici_liste = copy.deepcopy(yollar[indeks])
					gecici_liste.insert(0,deger)
					#print(gecici_liste)           
				elif sum(yollar[indeks]) < sum(yollar[indeks+1]):
					print (f"ikinci yol daha büyük,  {deger}, {yollar[indeks+1]}'e aktarılıyor...")
					gecici_liste = copy.deepcopy(yollar[indeks+1])
					gecici_liste.insert(0,deger)
					#print(gecici_liste)    
				else:
					print("HATA ! iki yol eşit. herhangi biri seçiliyor ")
					gecici_liste = copy.deepcopy(yollar[indeks+1])
					gecici_liste.insert(0,deger)
					#print(gecici_liste)
				yeniyollar.append(gecici_liste)
			yollar = copy.deepcopy(yeniyollar)
			#print(yeniyollar)
			print(f'\n\t{seviye}. katman incelenmesi tamamlandı...\n ---------------------------------------------------------- \n')
			seviye -=1
		print(sum(yeniyollar[0]), yeniyollar,sep='\n\t')

	a = time.time()
	#max_toplam(ucgen1)
	b = time.time()
	max_toplam(ucgen2)
	c = time.time() 
	#max_toplam(ucgen3)
	d = time.time()
	print(b-a, c-b, d-c)
def euler19():
	'''
	You are given the following information, but you may prefer to do some research for yourself.
	1 Jan 1900 was a Monday.
	Thirty days has September,
	April, June and November.
	All the rest have thirty-one,
	Saving February alone,
	Which has twenty-eight, rain or shine.
	And on leap years, twenty-nine.
	A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
	How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

	Size aşağıdaki bilgiler verilir, ancak kendiniz için biraz araştırma yapmayı tercih edebilirsiniz. 
	1 Ocak 1900 pazartesiydi. 
	Eylül, Nisan, Haziran ve Kasım ayları 30 gün. 
	Ocak Mart Mayıs Temmuz Ağustos Ekim Aralık 31 gün.
	Şubat: normalde 28 
	artık yıllarda, 29. 
	4 ün katları artık yıl (29 gün)
	100 ün katları artık yıl değil (28 gün) 
	400 ün katları artık yıl (29 gün)
	ancak 400'e bölünmediği sürece bir yüzyılda gerçekleşmez.
	Yirminci yüzyılda (1 Ocak 1901 - 31 Aralık 2000) ayın ilkine kaç Pazar düştü?

	'''
	
	g, hangigun, pazar_sayaci = -1,['Pazartesi', 'Sali', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar'], 0
	
	for yil in range(1900,2001):
		for ay in range(1,13):
			for gun in range(1,32):
				if ay in [4,6,9,11]:
					if gun == 31:
						break
				if ay == 2:
					if yil % 400 == 0:                              # .... 400'e bölündüğünde yani 1600 ve 2000'de şubat 29 gün
						if gun == 30:
							break
					elif yil % 100 == 0:							# ..... 400'ler hariç 100'e bölündüğünde 1700, 1800, 1900, 2100 28 gün
						if gun == 29:
							break
					elif yil % 4 == 0:								# ..... 100'ler hariç 4'e bölündüğünde 29 gün
						if gun == 30:
							break
					else:
						if gun == 29:								# ...... diğer yıllar 28 gün
							break
				g +=1
				if g == 7:
					g = 0			
				#print(f'{gun}.{ay}.{yil} - {hangigun[g]}')
				if yil >= 1901 and gun == 1 and hangigun[g] == 'Pazar' :
					print(f'{gun}.{ay}.{yil} - {hangigun[g]} \tAybaşı Pazar gününe denk geldi')
					time.sleep(0.05)
					pazar_sayaci += 1
	print(pazar_sayaci)
def euler20():
	'''	What is the sum of the digits of the number 100! '''
	
	def toplami(sayi,toplam=0):
		ax = 1
		while sayi > 1:
			ax *= sayi
			sayi -= 1
		while ax > 0:
			toplam += (ax%10)
			ax = ax//10
		return(toplam)
	 
	print(toplami(100))

#euler16()
#euler17()
euler18()
#euler19()
#euler20()
