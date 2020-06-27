def index_carpici(liste):
  	toplam = 0
    for i in range(len(liste)):
        toplam += liste[i]*i
    return toplam




print(index_carpici([-2,4,10,7,-9]))
