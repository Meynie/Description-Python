import socket # domain: port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5001)) #теперь сокет привязан к 5000 порту
server_socket.listen() #слушает на случай входящих подключений

while True:
    print('Before accept')
    # серверный сокет описан серху, теперь время клиентского сокета
    client_socket, addr = server_socket.accept() # читает данные из входящего буфера
    print('Connection from', addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode() # без аргументов кодирует строку в bites
            client_socket.send(response)

    print('Outside inner while loop')
    client_socket.close()
