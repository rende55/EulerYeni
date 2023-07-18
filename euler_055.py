def palindromik_mi(sayi):
    terS = int(str(sayi)[::-1])
    if sayi==terS:
        return True
    else:
        return False

def is_lychrel_number(sayimiz):
    terS = int(str(sayimiz)[::-1])
    sayimiz = sayimiz + terS
    sayac = 0
    while sayac <= 50:
        if palindromik_mi(sayimiz):
            #print(sayac)
            return False
        else:
            sayac+=1
            terS = int(str(sayimiz)[::-1])
            sayimiz = sayimiz + terS
    #print(sayac)
    return True

a = 0

for i in range(1,10_000):
    if is_lychrel_number(i):
        print(i)
        a+=1
print(a)


