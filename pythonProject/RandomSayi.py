import random

rastgele=round(random.random()*100)
print(rastgele)

girilen_sayi=int(input("0 ile 100 arası bir sayı girin="))

while rastgele!=girilen_sayi:
    if girilen_sayi>rastgele:
        print("Büyük girdiniz")
    else:
        print("Küçük girdiniz")

    girilen_sayi=int(input("0 ile 100 arası bir sayı girin="))

print("tebrikler oyunu kazandınız")

