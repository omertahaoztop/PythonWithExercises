# -*- coding: utf-8 -*-
def tekrarlanmayan(girdi):
    sonuc=list()
    for i in range(len(girdi)):
        if girdi.count(girdi[i])==1:
            sonuc.append(girdi[i])
    return sonuc        
    
    
    
    
print(tekrarlanmayan([2,2,3,11,3,6,5]))