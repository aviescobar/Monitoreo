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
  print(f"Servidor escuchando en {HOST}:{PORT}")

  while True:
    cliente_socket, direccion = servidor_socket.accept()
    print(f"Conexión recibida de {direccion}")

    # Recibir la solicitud del cliente
    solicitud = cliente_socket.recv(1024).decode()
    print(f"Solicitud:\n{solicitud}")

    # Extraer la página solicitada
    primera_linea = solicitud.splitlines()[0]
    pagina_solicitada = primera_linea.split(" ")[1]

    # Comprobar si la página está prohibida
    if pagina_solicitada in PAGINAS_PROHIBIDAS:
      respuesta = (
        "HTTP/1.1 403 Forbidden\r\n"
        "Content-Type: text/html\r\n\r\n"

