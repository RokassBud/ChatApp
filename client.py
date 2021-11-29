import socket

from threading import Thread


def receive():
	while True:
		try:
			print(csock.recv(BUFSIZ).decode())
		except OSError :
			break

def send():
	msg = input()
	csock.send(bytes(msg,'utf-8'))
	

HOST = 'localhost'
PORT = 9999
BUFSIZ = 512

csock = socket.socket()
csock.connect((HOST, PORT))

Thread(target=receive).start()
while True:
	send()



		