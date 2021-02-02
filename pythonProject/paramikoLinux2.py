import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("127.0.0.1",username="admin",password="password")
stdin,stdout,stderr=ssh.exec_command("cat /etc/passwd")

for i in (stdout.read().decode("ascii").split("\n")):
     try:
         if 0==int((str(i).split(":")[2])):
             print("uid 0 olan kullanıcı",str(i).split(":")[0])
     except:
        pass

#Linux'un doğru bir şekilde yapılandırılıp yapılandırılmadığını kontrol edebilirz
