# -*- coding: utf-8 -*-
def geri_say(n, yazı):
    cevap = ""
    for x in range(n):
        cevap = cevap + str(n-x) + ". "
    cevap = cevap + yazı.upper() + "!"
    return cevap

print(geri_say(7, "HEMEN!"))