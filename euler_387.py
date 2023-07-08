# PROBLEM NO.387 HARSHAND NUMBERS
'''


A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit, 
always results in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 1014.



'''
import time
import logging


logging.basicConfig(filename="387.log", format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def sum_of_digits(number):
    sum = 0
    while number > 0:
        remain = number % 10
        sum  += remain
        number = number//10
    return sum

#print(sum_of_digits(21))

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

def recursivelyTruncatable(number):
    while number > 0:
        number = number // 10
        if number == 0:
            return True
        digitS= sum_of_digits(number)
        #print(number,digitS)
        if number % digitS != 0:
            return False
    return True

def ssrHpn(limit):
    sumOfStrongRightTruncatableHarshadPrimes = 0
    for i in range(limit+1,10,-2):
        if i % 10_000_000_001 == 0:
            logging.warning(f'devam ediyor sayı = {i} süre = {saniyeCevir(time.process_time())}')
        if not recursivelyTruncatable(i):
            continue
        if not asal_mi(i):
            continue
        n = i//10
        sOD = sum_of_digits(n)
        if n % sOD != 0:
            continue
        if not asal_mi(int(n/sOD)):
            continue
        sumOfStrongRightTruncatableHarshadPrimes += i
        logging.warning(f'\n{i} sayısı şartları sağladı.\nToplam = {sumOfStrongRightTruncatableHarshadPrimes} \nSüre = {saniyeCevir(time.process_time())}\n')   
    logging.warning(f'Toplam({limit}) = {sumOfStrongRightTruncatableHarshadPrimes}')
    return sumOfStrongRightTruncatableHarshadPrimes

ssrHpn(10**10)


#ssrHpn(99750000009975)


