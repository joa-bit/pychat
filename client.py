import socket
HOST = '127.0.0.1'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while True:
	mensaje = input("Tu mensaje: ")
	mensaje = str.encode(mensaje)
	s.send(mensaje)
	print ("Esperando respuesta")
	respuesta = s.recv(1024)
	print ("Recibido: ", repr(respuesta))
s.close()