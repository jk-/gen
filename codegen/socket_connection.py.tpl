import socket


class SocketConnection(object):

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
        except:
            raise

    def send(self, command: str):
        self.socket.send(f'{command}'.encode('utf-8'))

    def receive(self):
        return self.socket.recv(1024).decode()
