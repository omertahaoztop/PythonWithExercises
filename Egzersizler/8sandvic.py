# -*- coding: utf-8 -*-
def sandviç(malzeme,secilen):
    cevap=list()
    for i in malzeme:
        if i == secilen:
            cevap.append("ekmek")
            cevap.append(i)
            cevap.append("ekmek")
        else:
            cevap.append(i)
        return cevap
            
        
    

    
print(sandviç(['peynir', 'salam'], 'peynir'))    