import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def loop_b():
	while True:
		respuesta = s.recv(1024)
		respuesta = respuesta.decode("utf-8")
		print (repr(respuesta))

Thread(target=loop_b).start()
while True:
	mensaje = str.encode(input(""))
	s.send(mensaje)


s.close()