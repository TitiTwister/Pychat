import socket, select, sys
import random
import users

def sign_in():
    
    client_connection.send("login ?")
    login = client_connection.recv(1024)
    if not user.check_login(login) :
        client_connection.send("I don't know you")
        client_connection.close()
    print(type(login))
    client_connection.send("password ?")
    password = client_connection.recv(1024)
    if not user.check_password(password) :
        client_connection.send("Wrong password m**********")
        client_connection.close()
    
    client_connection.send("Welcome !")

host = 'localhost'
port = random.randint(1024, 65535)
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind((host,port))
main_connection.listen(5)
client_connection, connection_info = main_connection.accept()


print("Server : %s now listen on %s port")%(host,port)

client_connection.recv(1024) #temp for respond

"""
USER CONNECTION
"""

user = users.User()
sign = 0

while sign !=1 :
    client_connection.send("Sign in : 1, sign up : 2, quit : 3")
    sign = int(client_connection.recv(1024))
    print(type(sign))
    
if sign == 1 :
    print("sign == 1 go for sign in")
    sign_in()
elif sign == 3 :
    client_connection.close()
   

"""
CHAT WITH CLIENT
"""
in_message = ""
while in_message != "over":
    in_message = client_connection.recv(1024)
    print(in_message.decode())
    client_connection.send("ok")
    
print("Closing connexion")
client_connection.close()
main_connection.close()

