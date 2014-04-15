import socket

class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print('sendind {0} to {1}'.format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()


    
def respond(client):
    response = input('name: ')
    client.send(bytes(response, 'utf8'))
    client.close;

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close;


    
