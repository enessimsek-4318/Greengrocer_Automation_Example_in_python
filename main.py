import time
import musteri
import toptanci
import manav
print("**************ENES ŞİMŞEK**************\n***********MANAV UYGULAMASI************")
ciksinMi= True
while ciksinMi:
    secim1=int(input("Manav Girişi   :1\nMüşteri Girişi :2\nÇıkış          :3\nLütfen Seçimizi Yapınız."))
    if secim1==1:
        kontrol= False
        if manav.sifreKontrol(manav.userName,manav.password):
            kontrol= True
        else:
            manav.hataliIslem()
        while kontrol:
            manavSecim = int(input("Toptancıdan Ürün Al :1\nÜrün Listele        :2\nAnamenüye Dön       :3\nLütfen Seçimizi Yapınız..."))
            if manavSecim==1:
                kontrol2=True
                while kontrol2:
                    secim2 = manav.tercih()
                    if secim2==1:
                        toptanci.listeleToptanciMeyve()
                        manav.urunEklemeMeyve(toptanci.urunlerMeyve)

                    elif secim2==2:
                        toptanci.listeleToptanciSebze()
                        manav.urunEklemeSebze(toptanci.urunlerSebze)

                    elif secim2==3:
                        kontrol2=False
                    else:
                        manav.hataliIslem()
            elif manavSecim==2:
                manav.manavListeleMeyve(manav.manavUrunMeyve)
                print("********************")
                manav.manavListeleSebze(manav.manavUrunSebze)
            elif manavSecim==3:
                kontrol=False
            else:
                manav.hataliIslem()
    elif secim1==2:
        manav.manavListeleMeyve(manav.manavUrunMeyve)
        print("********************")
        manav.manavListeleSebze(manav.manavUrunSebze)
        dongu=True
        while dongu:
            musteriSecim = musteri.musteriTercih()
            if musteriSecim==1:
                musteri.urunAl(manav.manavUrunMeyve,manav.manavUrunMeyveKg,manav.manavUrunSebze,manav.manavUrunSebzeKg)
            elif musteriSecim==2:
                musteri.sepetListele(musteri.sepet)
            elif musteriSecim==3:
                dongu=False

    elif secim1==3:
        ciksinMi= False
        print("Çıkış Yapılıyor...")
        time.sleep(2)
    else:
        manav.hataliIslem() # metodu main içine çekmek daha mantıklı


