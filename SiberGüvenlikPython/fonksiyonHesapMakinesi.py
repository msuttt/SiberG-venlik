def hesap_makinesi(s1,s2,islem):
    if islem == 1:
        sonuc=s1 + s2
    elif islem == 2:
        sonuc=s1 - s2
    elif islem == 3:
        sonuc = s1 * s2
    elif islem == 4:
        sonuc = s1 / s2
    else:
        sonuc="hata"

    return  sonuc

print(hesap_makinesi(1,4,2))