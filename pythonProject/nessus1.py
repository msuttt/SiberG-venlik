import requests
import subprocess #ilgili komutu terminalde çalıştırıp geri döndürür

header={"X-ApiKeys":"accessKey=81f3cc49d00838379cf57b974200d33ebefc88840d0ac7553defd7a03a4523; secretKey=4cbad646e0f9cbb3de329cd02e629ab7bf9a6593e913258492feb95b90a0d36;"}
url="https://192.168.1.100:8834/scans"

sonuc=requests.get(url=url,headers=header,verify=False)

#print(sonuc.json())

for i in sonuc.json()["scans"]:
    scan_id=i["id"]
    print(i["id"])
    url="https://192.168.1.100:8834/scans/"+str(i["id"])
    sonuc=requests.get(url=url,headers=header,verify=False)

    for i in sonuc.json()["hosts"]:
     try:
        IP=i['hostname']
        host_id=i['host_id']
        print(IP)
        print(host_id)
        print("----------------")
        url="https://192.168.1.100:8834/scans/"+str(scan_id)+"/hosts/"+str(host_id)+"/plugins/11936"
        zafiyet=requests.get(url=url,headers=header,verify=False)
        plugin_output=zafiyet.json()['outputs'][0]['plugin_output']
        print(plugin_output)

        if "Windows" in plugin_output:
            dizin=subprocess.check_output("dir",shell=True)#terminalde çalıştırıp ilgili çıktının dizine atanması sağlanır
            if not "windows.txt" in str(dizin):
                veri=str(IP)+"\n"
                dosya=open("windows.txt","w")
                dosya.write(veri)
                dosya.close()

            dosya=open("windows.txt","r")
            IP_control=dosya.read()
            dosya.close()
            if not str(IP) in IP_control:
                veri = str(IP) + "\n"
                dosya = open("windows.txt", "a")
                dosya.write(veri)
                dosya.close()

     except:
        pass