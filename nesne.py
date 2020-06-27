#!/usr/bin/python
# -*- coding: utf8 -*-
class personel():
    
    def __init__(self, ad = "Girilmedi", soyad = "Bilgi Yok", yas = 23 , maas = 4000): 
        self.ad =  ad 
        self.soyad = soyad 
        self.yas = yas
        self.maas = maas
        
    def bilgileri_goster(self):
        print("""        
        Ad :{}      
        Soyad :{}
        Yaş:{}
        Maaş :{}
        """.format(self.ad,self.soyad,self.yas,self.maas))
        
    def zam(self,miktar):
        print("Zam ekleniyor.")
        self.maas += miktar

personel1 = personel("Fatih","Öztürk")
print(personel1.bilgileri_goster())
personel1.zam(1000)
print(personel1.bilgileri_goster())