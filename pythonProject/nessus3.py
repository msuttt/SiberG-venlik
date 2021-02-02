import requests
import subprocess
import datetime
import sqlite3

cikti=subprocess.check_output("dir",shell=True)

if not "port.db" in str(cikti):
    conn=sqlite3.connect('port.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE portlar(port text,ip text,zaman text)''')
    c.close()

header={"X-ApiKeys":"accessKey=81f3cc49d00838379cf57b974200d33ebefc88840d0ac7553defd7a03a4523; secretKey=4cbad646e0f9cbb3de329cd02e629ab7bf9a6593e913258492feb95b90a0d36;"}
url="https://192.168.1.100:8834/scans"
sonuc=requests.get(url=url,headers=header,verify=False)

for i in sonuc.json()['scans']:
    scan_id=i['id']
    url="https://192.168.1.100:8834/scans"+str(scan_id)
    tarama=requests.get(url=url,headers=header,verify=False)
    for j in tarama.json()['hosts']:
       try:
        host_id=j['host_id']
        #14272 açık portları gösteriyor
        url="https://192.168.1.100:8834/scans/"+str(scan_id)+"/hosts/"+str(host_id)+"/plugins/11219"
        IP=requests.get(url=url,headers=header,verify=False)
        for k in IP.json()['outputs']:
            port=list(k['ports'].keys())[0]
            IP=j['hostname']
            conn=sqlite3.connect("port.db")
            c=conn.cursor()
            cikti=c.execute('SELECT * FROM portlar where port=? and ip=?,(port,IP)')
            port_sayisi=len(cikti.fetchall())
            conn.close()
            if port_sayisi<1:
                print("yeni port:",port,"IP:",IP)
                conn=sqlite3.connect("port.db")
                c=conn.cursor()
                c.execute('INSERT INTO portlar values(?,?,?)',(port,IP,str(datetime.datetime.now())))
                conn.commit()
                conn.close()

       except:
           pass