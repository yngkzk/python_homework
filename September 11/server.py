import socket


class UDP_server:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Почему-то без этой линии сервер не запускается
# Но если убрать эту строку и запустить сначала client.py, а потом server.py, то сервер спокойно начинает работу

    def __init__(self, port=9900):
        self.port = port

    def start(self):

        server_address = ('127.0.0.1', self.port)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(server_address)

        while True:
            data, addr = server_socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            print(f'Message received from {addr}: {message}')

            if self.stop(message):
                break

            sender_ip, sender_port = addr[0], addr[1]
            reply_message = 'OK'
            server_socket.sendto(reply_message.encode(), (sender_ip, sender_port))

    def stop(self, message='exit'):  # Я не знаю как было бы лучше реализовать метод stop()
        if message == 'exit':
            return True
        return False


if __name__ == '__main__':
    my_server = UDP_server(9900)
    my_server.start()
    my_server.stop()
