import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("127.0.0.1",username="admin",password="password")
stdin,stdout,stderr=ssh.exec_command("ls")
print(stdout.read())
#linux sisteme bağlanıp linux komutu çalıştırıyor

