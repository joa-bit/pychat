
import socket

HOST = '127.0.0.1'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen(1) 
conn, addr = s.accept()
print ('Conectado por', addr)


while True:
	data = conn.recv(1024)
	print ("Recibido: ", repr(data))
	respuesta = input("Respuesta: ")
	respuesta = str.encode(respuesta)
	conn.sendall(respuesta)

conn.close()