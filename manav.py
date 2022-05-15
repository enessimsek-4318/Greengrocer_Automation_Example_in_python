import toptanci

manavUrunMeyve =[]
manavUrunMeyveKg=[]
manavUrunSebze=[]
manavUrunSebzeKg=[]
userName="enes4318"
password="enes"

def sifreKontrol(x,y):
    userNameGelen=input("Kullanıcı Adınızı Giriniz:")
    passwordGelen=input("Şifrenizi Giriniz:")
    if (userNameGelen==x) and (passwordGelen==y):
        print("Giriş Başarılı")
        return True
    else:
        return False
def tercih():
    return int(input("Meyve  :1\nSebze  :2\nGeri   :3\nLütfen Seçiminizi Yapınız."))

def urunEklemeMeyve(liste):
    devam=True
    while devam:
        indexNo = int(input("Lütfen Eklemek İstediğiniz Ürünün Numarasını Giriniz:"))
        if manavUrunMeyve.__contains__(liste[indexNo - 1]):
            kgBilgisi = int(input("Kaç Kilo Eklemek İstersiniz ?"))
            manavUrunMeyveKg[indexNo - 1] += kgBilgisi
        else:
            manavUrunMeyve.append(liste[indexNo - 1])
            kgBilgisi = int(input("Kaç Kilo Eklemek İstersiniz ?"))
            manavUrunMeyveKg.append(kgBilgisi)
        cikis1 = int(
            input("Satın Alma İşlemine Devam Etmek İçin (1) Satın Alma İşleminden Çıkmak İçin (2) Tuşlayınız."))
        if cikis1==1:
            devam=True
        elif cikis1==2:
            devam=False
        else:
            devam=False
def urunEklemeSebze(liste):
    devam=True
    while devam:
        indexNo=int(input("Lütfen Eklemek İstediğiniz Ürünün Numarasını Giriniz:"))
        if manavUrunSebze.__contains__(liste[indexNo-1]):
            kgBilgisi= int(input("Kaç Kilo Eklemek İstersiniz ?"))
            manavUrunSebzeKg[indexNo-1]+=kgBilgisi
        else:
            manavUrunSebze.append(liste[indexNo-1])
            kgBilgisi = int(input("Kaç Kilo Eklemek İstersiniz ?"))
            manavUrunSebzeKg.append(kgBilgisi)
        cikis1=int(input("Satın Alma İşlemine Devam Etmek İçin (1) Satın Alma İşleminden Çıkmak İçin (2) Tuşlayınız."))
        if cikis1==1:
            devam=True
        elif cikis1==2:
            devam=False
        else:
            devam=False

def manavListeleMeyve(manavListeMeyve):
    sayac=0
    for i in manavListeMeyve:
        sayac+=1
        txt="{} :"
        print(txt.format(sayac)+i)
def manavListeleSebze(manavListeSebze):
    sayac=0
    for i in manavListeSebze:
        sayac+=1
        txt="{} :"
        print(txt.format(sayac)+i)

def hataliIslem():
    print("Eksik veya Hatalı Giriş:")

