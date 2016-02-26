import socket
import signal
import sys

host = 'localhost'
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.connect((host,port))

print("Connection on with server")

out_message = " "

while out_message != "over":
    try:
        out_message = raw_input("> ")
        main_connection.send(out_message.encode())
        in_message = main_connection.recv(1024)
        print(in_message.decode())
        
    except KeyboardInterrupt:
        out_message = "over"
        main_connection.send(out_message.encode())
        raise
        
print("Closing connection")
main_connection.close()
                        