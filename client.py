import socket

# IP del Socket
TCP_IP = "127.0.0.1"
# Puerto del Socket
TCP_PORT = 1111

condicion = True

def mandarmensaje(enchufe):
	# Le pedimos al usuario ingresar el mensaje
	MESSAGE = raw_input("Mensaje a mandar: ")
	# Mandar mensaje
	enchufe.send(MESSAGE)
	if MESSAGE == "bye":
		return False
	# Recivimos la respuesta del Servidor
	data = enchufe.recv(4096)
	print "Recibi la respuesta: " + data
	return True

def conection(TCP_IP, TCP_PORT):
	# AF_INET = IPv4, SOCK_STREAM = Stream de Datos
	enchufe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Hacemos conection con el Server
	enchufe.connect((TCP_IP, TCP_PORT))
	return enchufe

conexion = conection(TCP_IP, TCP_PORT)

while condicion:
	respuesta = raw_input("\nDesea mandar un mensaje? (s/n): ")
	if respuesta == 's':
		condicion = mandarmensaje(conexion)
	elif respuesta == 'n':
		# Cierra la conexion
		conexion.close()
		condicion = False
	else:
		print "Solo se acepta un /'s/' o /'n/'como respuesta. \n"