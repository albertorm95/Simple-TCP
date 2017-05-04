import socket

def servidor():
	# IP del Socket
	TCP_IP = "127.0.0.1"
	# Puerto del Socket
	TCP_PORT = 1111
	# AF_INET = IPv4, SOCK_STREAM = Stream de Datos
	enchufe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Timeout
	enchufe.settimeout(60)
	print "\nEn " + str(60) + " segundos el servidor cerrara."
	# Enlazamos los dos sockets, el que recibe debe tener el .bind()
	enchufe.bind((TCP_IP, TCP_PORT))
	# Server espera una conection
	enchufe.listen(1)
	return enchufe

serverEnchufe = servidor()
while 1:
	# conn = new Scoket object, addr = Address bound to the scoket
	print "Esperando conexion..."
	conn, addr = serverEnchufe.accept()
	print "Connection Address:", addr
	# While para recibir mensajes
	while 1:
		conn.setblocking(1)
		data = conn.recv(4096)
		if not data:
			break
		elif data == "bye":
			conn.close()
			break
		else:
			print "Mensaje recibido: " + data
			# echo the message
			conn.send(data)