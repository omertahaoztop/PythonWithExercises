# -*- coding: utf-8 -*-
def zip(yazi):
    sayilan=yazi.count("zip")
    if sayilan<2:
        return -1
    else:
        ilk=yazi.find("zip")
        return yazi.find("zip",ilk+1)
    

    
    
print(zip("Birinci zip bu iken ikinci zip budur."))    