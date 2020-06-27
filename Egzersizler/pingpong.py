# -*- coding: utf-8 -*-
def ping_pong(liste,kazanma):
    sonuc = ["Ping!","Pong"]*len(liste)
    if kazanma:
        return sonuc
    else:
        return sonuc[:-1]
    
    
    
    
print(ping_pong(["Ping!", "Ping!", "Ping!","Ping!"], False))   
