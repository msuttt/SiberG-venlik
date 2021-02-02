sayi=int(input("Kaça kadar asal sayı bulunacak="))
print(2)

sayici=1
sayac=0
for i in range(3,sayi,1):
    kontrol=False

    for j in range(2,i):
        if i%j==0:
            kontrol=True

    if kontrol==False:
        print(i)




