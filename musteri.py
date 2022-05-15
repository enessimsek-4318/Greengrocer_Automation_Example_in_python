import manav
import musteri

sepet=[]
def musteriUrunListeMeyve(list):
    print("*****MEYVE*****")
    sayac=0
    for i in list:
        sayac+=1
        txt="{} :"
        print(txt.format(sayac)+i)
def musteriUrunListeSebze(list):
    print("*****SEBZE*****")
    sayac=0
    for i in list:
        sayac+=1
        txt="{} :"
        print(txt.format(sayac)+i)

def musteriTercih():
    musteriTercih1=int(input("Alışveriş Yap :1\nSepetim       :2\nAnamenü       :3"))
    return musteriTercih1

def sepetListele(x):
    print("*****SEPETİNİZ*****")
    sayac = 0
    for i in x:
        sayac += 1
        txt = "{} :"
        print(txt.format(sayac) + i)

def urunAl(x,y,a,b):
    musterisecim=int(input("Meyve :1\nSebze :2\nGeri  :3"))
    if musterisecim==1:
        devam=True
        while devam:
            indexNo=int(input("Lütfen Almak İstediğiniz Ürünün Numarasını Giriniz:"))
            if sepet.__contains__(x[indexNo-1]):
                kgBilgisi=int(input("Kaç Kilo Almak İstersiniz:"))
                y[indexNo-1]-=kgBilgisi
                if y[indexNo-1] <=0:
                    print("Ürün Tükenmiştir.")

            else:
                sepet.append(x[indexNo-1])
                kgBilgisi = int(input("Kaç Kilo Almak İstersiniz:"))
                y[indexNo - 1] -= kgBilgisi
                if y[indexNo - 1] <= 0:
                    print("Ürün Tükenmiştir.")

            cikis1=int(input("Satın Alma İşlemine Devam Etmek İçin (1) Satın Alma İşleminden Çıkmak İçin (2) Tuşlayınız."))
            if cikis1==1:
                devam=True
            elif cikis1==2:
                devam=False
            else:
                devam=False
    elif musterisecim==2:
        devam = True
        while devam:
            indexNo = int(input("Lütfen Almak İstediğiniz Ürünün Numarasını Giriniz:"))
            if sepet.__contains__(a[indexNo - 1]):
                kgBilgisi = int(input("Kaç Kilo Almak İstersiniz:"))
                b[indexNo - 1] -= kgBilgisi
                if b[indexNo - 1] <= 0:
                    print("Ürün Tükenmiştir.")

            else:
                sepet.append(a[indexNo - 1])
                kgBilgisi = int(input("Kaç Kilo Almak İstersiniz:"))
                b[indexNo - 1] -= kgBilgisi
                if b[indexNo - 1] <= 0:
                    print("Ürün Tükenmiştir.")

            cikis1 = int(
                input("Satın Alma İşlemine Devam Etmek İçin (1) Satın Alma İşleminden Çıkmak İçin (2) Tuşlayınız."))
            if cikis1 == 1:
                devam = True
            elif cikis1 == 2:
                devam = False
            else:
                devam = False