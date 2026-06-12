# SOCKETS RESEAU : SERVEUR

# socket
# bind (ip, port) 127.0.0.1 -> localhost
# listen
# accept -> socket / (ip, port)
# close

import socket
HOST_IP = "127.0.0.1"
HOST_PORT = 32000

serveur = socket.socket()
serveur.bind((HOST_IP, HOST_PORT))
serveur.listen()
print(f"Serveur en attente de connexion sur le port {HOST_PORT}, port {HOST_PORT}...")
connexion_socket, adresse_client = serveur.accept()
print(f"Connexion établie avec {adresse_client}")