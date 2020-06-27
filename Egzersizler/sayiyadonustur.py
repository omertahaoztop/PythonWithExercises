# -*- coding: utf-8 -*-
def gercek_deger(oylar):
    cevap=list()
    degerler=oylar.split()
    for i in degerler:
        if "k" not in i:
            cevap.append(int(i))
        else:
            gercek=i.replace("k","00").replace(".","")
            cevap.append(int(gercek))
    return cevap       
            
        
    
    
    
    

print(gercek_deger("2.1k 321 23.1k"))    
