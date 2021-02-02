import socket

host="0.0.0.0"
port=5000
socket=socket.socket()
socket.bind((host,port))
socket.listen()
conn,addr=socket.accept()
print("Bağlandı",str(conn))
mesaj="Bağlantı sağlandı".encode()
conn.send(mesaj)
while True:
    komut=input("komut=")
    conn.send(komut.encode())
    if komut.lower()=="exit":
        break
    sonuc=conn.recv(5000).decode()
    print(sonuc)
conn.close()
socket.close()


