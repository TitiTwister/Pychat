import socket, select, sys
import random

host = 'localhost'
port = random.randint(1024, 65535)

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

main_connection.bind((host,12800))

main_connection.listen(5)

client_connection, connection_info = main_connection.accept()

print("Server : %s now listen on %s port")%(host,12800)

in_message = ""
while in_message != "fin":
    in_message = client_connection.recv(1024)
    print(in_message.decode())
    client_connection.send("5/5")
    
print("Closing connexion")
client_connection.close()
main_connection.close()









#print(main_connection)