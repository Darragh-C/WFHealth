import socket
import logging

logging.basicConfig(level=logging.INFO)

# Host side UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Port to listen for UPD datagrams
port=1235

# Bind server socket to the port
serverSocket.bind(('', port))
print("Server listening on port "+ str(port))
logging.info(f"Server listening on port: {str(port)}")
while True:
    message, address = serverSocket.recvfrom(1024)
    print(message)
    logging.info(f"Received message: {message}")