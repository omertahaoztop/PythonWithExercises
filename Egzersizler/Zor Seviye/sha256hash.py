# -*- coding: utf-8 -*-
import hashlib
def sha256_hash(şifre):
    kod=hashlib.sha256(şifre.encode())
    return kod.hexdigest()
    
    

print(sha256_hash("şifrembu"))