import SocketServer, socket
import logging
import sys 
import users
import threading

logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s',)

class Chat_Handler(SocketServer.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('Chat')
        self.user = users.User()
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return
    
    def handle(self):
        self.logger.debug('Connection from : %s', self.client_address)
        if not self.sign_in() :
            return

        in_message = " "
        while in_message != "over" :
            in_message = self.request.recv(1024).decode()
            self.logger.debug('%s -> "%s"',self.client_address[0], in_message)
            self.request.send("vu")
        return

    def finish(self):    
        self.logger.debug('Connection stopped with : %s'%self.client_address[0])
        return SocketServer.BaseRequestHandler.finish(self)

    def sign_in(self):
        self.request.send("login ?")
        login = self.request.recv(1024)
        if not self.user.check_login(login) :
            self.request.send("I don't know you")
            return False
        
        self.request.send("password ?")
        password = self.request.recv(1024)
        if not self.user.check_password(password) :
            self.request.send("Wrong password m**********")
            return False
        
        self.request.send("Welcome !")
        return True

class Chat_server(SocketServer.TCPServer):
    
    def __init__(self, server_address, handler_class=Chat_Handler):
        self.logger = logging.getLogger('Server')
        self.logger.debug('__init__')
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return
    
    def server_activate(self):
        self.logger.debug('server_activate')
        SocketServer.TCPServer.server_activate(self)
        return
   
class Chat_thread_server(SocketServer.ThreadingMixIn, Chat_server): 
    pass
    
if __name__ == '__main__':
    
    address = ('', 12800)
    server = Chat_thread_server(address, Chat_Handler)
    server.serve_forever()
    ip, port = server.server_address 
    logger = logging.getLogger('server')
    logger.info('Server listen on %s:%s', ip, port)
    

"""
USER CONNECTION

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
   
    