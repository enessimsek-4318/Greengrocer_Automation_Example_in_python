urunlerMeyve=["Elma", "Armut", "Kiraz", "Muz", "Çilek", "Şeftali", "Vişne", "Mango", "Üzüm"]
urunlerSebze=["Soğan", "Sarımsak", "Biber", "Salatalık", "Domates", "Patlıcan", "Patates","Pırasa","Kabak"]

def listeleToptanciMeyve():
    sayac=0
    for i in urunlerMeyve:
        sayac+=1
        txt="{} :"
        print(txt.format(sayac)+i)
def listeleToptanciSebze():
    sayac=0
    for i in urunlerSebze:
        sayac+=1
        txt="{} :"
        print(txt.format(sayac)+i)
