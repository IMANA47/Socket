import socket
import time
HOST_IP = "127.0.0.1"   
HOST_PORT = 32000
MAX_DATA_SIZE = 1024
client = socket.socket()

while True:
    try:
        client.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("Connexion au serveur impossible.")
        time.sleep(4)
    else:
        print("Connexion établie avec le serveur.")
        break

data_recu = client.recv(MAX_DATA_SIZE)
if not data_recu:
    print("Aucun message reçu du serveur.")
else:
    print(f"Message reçu du serveur : {data_recu.decode()}")
client.close()
