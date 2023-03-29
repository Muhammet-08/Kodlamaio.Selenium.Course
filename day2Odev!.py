ogrenciListesi=[]

def ogrenciEkle():
    adSoyad=input("Eklenmek istediğiniz öğrencinin ad soyadını giriniz")
    ogrenciListesi.append(adSoyad)
    if adSoyad==adSoyad:
        ogrenciListesi.remove(adSoyad)
        ogrenciListesi.append(adSoyad)
        print("Öğrenci aynı ad ve soyada sahip olduğu için sistemdeki silinip yenisi eklenmiştir!")

    print("Öğrenci eklenmiştir.")
    print(adSoyad)

def ogrenciListele():
    print("Öğrenciler Listeleniyor.")
    ogrenci=0
    for ogrenci in ogrenciListesi:
        print(ogrenci)
    
def ogrenciSil():
    adSoyad=input("Silmek istediğiniz öğrencinin adını ve soyadını giriniz.")
    ogrenciListesi.remove(adSoyad)
    print("Sildiğiniz öğrenci:"+adSoyad)
    print("Öğrenciler Siliniyor !!!")


def birdenFazlaOgrenciEkle():
    kac=int(input("Kaç tane öğrenci eklemek istersiniz."))
    i=0
    while i<kac:
        print(f"{i+1}.ci öğrenciyi ekle. ")
        ogrenciEkle()
        i+=1
        print(f"{i} tane öğrenci başarılı bir şekilde eklenmiştir.")

def numaradanOgrenciBul():
    adSoyad=input("Numarasını öğrenmek istediğiniz öğrencinin ad ve soyadını giriniz !!!")
    ogrNo=ogrenciListesi.index(adSoyad)
    print(adSoyad+"adlı öğrencinin numarası:"+str(ogrNo+1))

def birdenFazlaOgrenciSil():
    kac=int(input("Kaç tane öğrenci silmek istersiniz ?\n"))
    i=0
    while i<kac:
        print(f"{i+1}.öğrenciyi sil.")
        ogrenciSil()
        i+=1
        print(f"{i} tane öğrenci başarıyla silinmiştir.")


birdenFazlaOgrenciEkle()
ogrenciListele()
birdenFazlaOgrenciSil()
ogrenciListele()
numaradanOgrenciBul()
ogrenciListele()




