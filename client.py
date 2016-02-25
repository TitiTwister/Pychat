import socket

host = 'localhost'
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.connect((host,port))

print("Connection on with server")

out_message = ""

while out_message != "fin":
    out_message = raw_input("> ")
    
    out_message = out_message.encode()
    
    main_connection.send(out_message)
    in_message = main_connection.recv(1024)
    print(in_message.decode())

print("main connection closing")
main_connection.close()
                        