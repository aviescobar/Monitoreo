import socket


# Configuración del servidor
HOST = '0.0.0.0'  # Dirección IP del servidor
PORT = 8080         # Puerto en el que el servidor escuchará

# Lista de páginas prohibidas
PAGINAS_PROHIBIDAS = ["/prohibido.html", "/privado.html"]


def servidor():
  # Crear el socket del servidor
  servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servidor_socket.bind((HOST, PORT))
  servidor_socket.listen(5)

