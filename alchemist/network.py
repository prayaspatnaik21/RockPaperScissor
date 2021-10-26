import socket

class Network:
    def _init_(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.11"
        self.port = 12345
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

n = Network()