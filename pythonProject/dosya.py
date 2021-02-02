for i in range(1,10,1):
   dosya=open("sayılar.txt","a") # a=append
   veri=str(i)+"\n"
   dosya.write(veri)
   dosya.close()

   # ifadenin teker teker eklenmesi için append mode
   # sadece o dosyaya veri yazdırmak için write mode