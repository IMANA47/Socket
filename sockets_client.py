import socket
HOST_IP = "127.0.0.1"   
HOST_PORT = 32000

client = socket.socket()
try:
    client.connect((HOST_IP, HOST_PORT))
    print(f"Connexion au serveur {HOST_IP} sur le port {HOST_PORT}...")
    print("Connexion établie avec le serveur.")
except ConnectionRefusedError:
    print("Connexion au serveur impossible.")
finally:
    client.close()
