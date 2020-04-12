#!/usr/bin/env python3

from enum import Enum
import bluetooth

class SocketState(Enum):
	OPENED = 1
	CONNECTED = 2
	CLOSED = 3

def main():
	server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	port = 1
	server_sock.bind(("",port))
	server_sock.listen(1)
	print("listening on port %d" % port)

	uuid = "3f9af32c-548f-4152-87b9-46ea997b22b5"

	bluetooth.advertise_service( server_sock, "Service", uuid )

	socketState = SocketState.OPENED
	while socketState == SocketState.OPENED:

		print("Waiting for a connection")
		client_sock,address = server_sock.accept()
		print("Accepted connection from ", address)

		socketState = SocketState.CONNECTED 
			
		while socketState == SocketState.CONNECTED :
			try:
				print("receiving message")
				data = client_sock.recv(1024)
				if data == "CLOSE_CONNECTION":
					socketState = SocketState.CLOSED
				print("received [%s]" % data)
			except bluetooth.btcommon.BluetoothError as ex:
				print( ex )

		if socketState == SocketState.CLOSED:
			client_sock.close()
			socketState = SocketState.OPENED

	server_sock.close()

if __name__ == "__main__":
    main()

