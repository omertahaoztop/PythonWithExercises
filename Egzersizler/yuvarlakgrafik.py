# -*- coding: utf-8 -*-
def pasta_grafigi(veri):
    toplam=0
    for kategori in veri:
        toplam+=veri[kategori]
    for kategori in veri:
        veri[kategori]/=toplam
        veri[kategori]=round(veri[kategori]*360,1)
    return veri

print(pasta_grafigi({ "a": 4, "b":7 }))