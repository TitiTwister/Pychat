import SocketServer, socket
import logging
import sys 
import users

logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s',)

class Chat_Handler(SocketServer.BaseRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('Chat_Handler')
        self.logger.debug('__init__ handler')
        self.user = users.User()
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        return
    
    def handle(self):
        self.logger.debug('handle')
        self.logger.debug(self.client_address[0])
        self.sign_in()
        data = " "
        while data != "over" :
            
            data = self.request.recv(1024).decode()
            self.logger.debug('recv()->"%s"', data)
            self.request.send(data)
        return

    def finish(self):    
        self.logger.debug('finish handler with : %s'%self.client_address[0])
        return SocketServer.BaseRequestHandler.finish(self)

    def sign_in(self):
        self.request.send("login ?")
        login = self.request.recv(1024)
        if not self.user.check_login(login) :
            self.request.send("I don't know you")
            self.finish()
        
        self.request.send("password ?")
        password = self.request.recv(1024)
        if not self.user.check_password(password) :
            self.request.send("Wrong password m**********")
            self.finish()
        
        self.request.send("Welcome !")

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
    
    
    
if __name__ == '__main__':

    address = ('localhost', 12800) # let the kernel give us a port
    server = Chat_server(address, Chat_Handler)
    server.serve_forever()
    ip, port = server.server_address # find out what port we were given
    logger = logging.getLogger('server')
    logger.info('Server on %s:%s', ip, port)



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
   
    