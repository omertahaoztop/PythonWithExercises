# -*- coding: utf-8 -*-
def kac_tane(başlangıç,bitiş,sayı):
    liste=[]
    for i in range(başlangıç,bitiş+1):
        liste.append(str(i))
    cevap=0
    for i in range(len(liste)):
        cevap+=liste[i].count(str(sayı))
    return cevap    
    
    
print(kac_tane(1, 67, 7))