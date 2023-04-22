
import socket
import sys
import juego
juego
# Crear socket
socketConexion = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
# Servidor de conexión
servidor = "localhost"
# El puerto a utilizar (el servidor debe estar escuchando en este puerto)
puerto = 8080

msg = "Hola mundo de cliente" + "\r\n"
socketConexion.sendto(msg.encode(),(servidor,puerto))

# Cerrar el socket
socketConexion.close()