from server import UdpServer
from client import UdpClient

# Не работает

if __name__ == '__main__':
    server = UdpServer(9900)
    client = UdpClient('127.0.0.1', 9900)

    server.start()
    client.send('Hallo')
    client.receive()
    server.stop()
