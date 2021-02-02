veri="Eğitim 101"
egitim=list(veri)
print(egitim)

harf_sayici=0
rakam_sayici=0

for i in egitim:
    if str(i).isdecimal():
        rakam_sayici+=1
    else:
        harf_sayici+=1
print("rakam sayısı=" ,rakam_sayici)
print("harf sayısı=" , harf_sayici)
