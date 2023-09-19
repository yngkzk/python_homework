import socket


class UdpClient:
    address = 'localhost'
    port = 0
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, address, port):
        self.address = address
        self.port = port

    def send(self, message):
        server_address = (self.address, self.port)

        self.server_socket.sendto(message.encode(), server_address)

    def receive(self):
        data, addr = self.server_socket.recvfrom(1024)
        print('Response from the server:', data.decode(encoding='UTF-8'), sep=' ')


if __name__ == '__main__':
    client = UdpClient('127.0.0.1', 9900)
    client.send('hallo')
    client.receive()
