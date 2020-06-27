# -*- coding: utf-8 -*-
def buyuk_kucuk(deger):
    yeni=deger.split()
    yeni=[int(i) for i in yeni]
    buyuk=max(yeni)
    kucuk=min(yeni)
    return str(buyuk)+" " + str(kucuk)

print(buyuk_kucuk("3 2 4 6 -1 12"))

    
    
    
    
    
    
