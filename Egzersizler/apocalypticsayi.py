# -*- coding: utf-8 -*-
def is_apocalyptic(sayi):
    x=str(pow(2,sayi))
    if x.count("666")==0:
        return "GÜvenli"
    elif x.count("666")==1:
        return "Tek"
    elif x.count("666")==2:
        return "çift"
    elif x.count("666")==3:
        return "Üçlü"
    

    
print(is_apocalyptic(651))