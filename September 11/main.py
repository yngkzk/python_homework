from server import UDP_server
from client import UDP_client

# Не работает

if __name__ == '__main__':
    server = UDP_server(9900)
    client = UDP_client('127.0.0.1', 9900)

    server.start()
    client.send('Hallo')
    client.receive()
    server.stop()
