import socket
from threading import Thread


def waiting_for_connection():
	while True:
		client, client_adress = SERVER.accept()
		print("Connected: ", client_adress)
		client.send(bytes("Enter your name","utf8"))
		addresses[client] = client_adress 
		Thread(target=communicating, args=(client,)).start()

def communicating(client):
	name = client.recv(BUFSIZ).decode("utf8")
	client.send(bytes("Welcome! If you ever want to quit, type {quit} to exit.", "utf8"))
	msg = f"{name} has joined the chat"
	broadcast(bytes(msg, "utf8"))
	clients[client] = name
	while True:
		msg = client.recv(BUFSIZ)
		if msg != (bytes("{quit}", "utf8")):
			broadcast(msg, name +": ")
		else:
			client.send(bytes("{quit}", "utf8"))
			SERVER.close()
			del clients[client]
			boardcast(bytes(f"{name} left the chat","utf8"))
			break

def broadcast(msg, prefix=''):
	for sock in clients:
		sock.send(bytes(prefix,"utf8")+msg)


clients = {}
addresses = {}

HOST = 'localhost'
PORT = 9999
BUFSIZ = 512

SERVER = socket.socket()
SERVER.bind((HOST,PORT))
print("Socket created")


if __name__ == "__main__":
	SERVER.listen(3)
	print("Waiting for connection...")
	ACCEPT_THREAD = Thread(target=waiting_for_connection)
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()
