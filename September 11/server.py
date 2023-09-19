import socket


class UdpServer:

    def __init__(self, port=9900):
        self.port = port
        self.server_address = ('127.0.0.1', self.port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(self.server_address)
        self.is_enabled = True

    def start(self):
        while self.is_enabled:
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            print(f'Message received from {addr}: {message}')
            sender_ip, sender_port = addr[0], addr[1]
            reply_message = 'OK'
            self.server_socket.sendto(reply_message.encode(), (sender_ip, sender_port))

    def stop(self, message='exit'):
        if message == 'exit':
            self.is_enabled = False
            return self.is_enabled
        return False


if __name__ == '__main__':
    my_server = UdpServer(9900)
    my_server.start()
    my_server.stop()
