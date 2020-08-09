import socket
from threading import Thread



HOST = '127.0.0.1'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen(1) 
conn, addr = s.accept()
print ('Conectado por', addr)

def loop_b():
	while True:
		data = conn.recv(1024)
		data = data.decode("utf-8")
		print (repr(data))

Thread(target=loop_b).start()
while True:
    respuesta = str.encode(input(""))
    conn.sendall(respuesta)



conn.close()