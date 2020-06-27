# -*- coding: utf-8 -*-
def eklemeli_devamlılık(n):
    işlem=0
    while n>9:
        n=sum(int(i) for i in str(n))
        işlem+=1
    return işlem
def carpan(n):
    carp=1
    for i in str(n):
        carp*=int(i)
    return carp    
    
    
    
def çarpan_devamlılığı(n):
    işlem=0
    while n>9:
        n=carpan(n)
        işlem+=1
    return işlem


print(çarpan_devamlılığı(512)*eklemeli_devamlılık(512))    

