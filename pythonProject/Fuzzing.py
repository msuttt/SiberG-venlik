import requests


dosya=open("Fuzzing.txt","r")
icerik=dosya.read()
dosya.close()
#header="burp suite programından birşey aldı";
for i in icerik.split("\n"):
    print(i)
    url="http://127.0.0.1"+str(i)
    sonuc=requests.get(url=url)#header kullanmazsak kullanıcı girişi olmadan ilgili dosyaları gösterir,header kullanırsak kullanıcıların görebileceği dosyaları gösterir
    if "200" in str(sonuc.status_code):
        print("dosya veya dizin var",i)
    else:
        print("dosya veya dizin yok",i)