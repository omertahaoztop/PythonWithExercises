# -*- coding: utf-8 -*-
def dogru_format_mı(telefon):
    p1 = telefon[1:4] + telefon[6:9] + telefon [10:]
    p2 = telefon[0] + telefon[4]
    p3 = telefon[5]
    p4 = telefon[9]
    evetTelefon=True
    if p1.isdigit() and p2=="()" and p3 ==" "and p4== "-":
        return evetTelefon
    else:
        return not evetTelefon
print(dogru_format_mı("(543) 351-7391"))
