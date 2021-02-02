a_sinifi=["Ahmet","Mehmet"]
b_sinifi=["Ayşe","Fatma"]
isim=input("isim giriniz=")

if isim in a_sinifi:
    print(str(isim) ,"a sınıfındadır")
elif isim in b_sinifi:
    print(str(isim) , "b sınıfındadır")
else:
    print(str(isim) ,"sınıflarda bulunmamaktadır")