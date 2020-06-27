#!/usr/bin/env python
# -*- coding: utf-8 -*-
def say(yazi):
	ara=yazi.lower()
	harfler=set("abcçdefgğhıijklmnoöprsştuüvyz")
	rakam=set("0123456789")
	sayilanHarf=0
	sayilanRakam=0
 	for karakter in ara:
     if karakter in harfler:
         sayilanHarf+=1
	elif karakter in rakam:
		 sayilanRakam+=1
return {"Harfler":,sayilanHarf,"Sayılar":sayilanRakam}	

