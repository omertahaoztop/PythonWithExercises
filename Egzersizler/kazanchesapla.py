# -*- coding: utf-8 -*-
def kazanc(bilgi):
    a=bilgi["maliyet"]
    b=bilgi["satış"]
    c=bilgi["envanter"]
    toplam_maliyet=a*c
    toplam_satis=b*c
    kazanc=round(toplam_satis-toplam_maliyet)
    return kazanc




print(kazanc({"maliyet": 1.33,"satış": 2.45,"envanter": 1023}))
