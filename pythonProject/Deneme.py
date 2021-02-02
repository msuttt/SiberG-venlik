s1=int(input("ilk sayıyı girin="));
s2=int(input("ikinci sayıyı girin="));

toplam=int(s1+s2);

print("sonuc=",toplam);

if toplam>10:
    print("10 dan büyük");
else:
    print("10 dan küçük");

sayi=int(input("sayı girin="));

for i in range(0,sayi,1):
    print(i);

while sayi<toplam:
   print("sayi hala toplamdan büyük değil");
   sayi=sayi+1;

   dosya=open("deneme.txt","w");
   string="Mesut";
   dosya.write(string);
   dosya.close();

   dosya1=open("deneme.txt","r");
   icerik=dosya1.read();
   dosya.close();
   print(icerik);
