# Основные рабочие функции работают независимо друг от друга

import socket # domain: port
from select import select # мониторит изменения файловых объектов (сокетов), который в нее передали

to_monitor = []

# создаю серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5001)) #теперь сокет привязан к 5000 порту
server_socket.listen() #слушает на случай входящих подключений


# передаю в функцию, где создаю клиентский сокет
def accept_connection(server_socket):
    # серверный сокет описан серху, теперь время клиентского сокета
    client_socket, addr = server_socket.accept() # читает данные из входящего буфера
    print('Connection from', addr)

    to_monitor.append(client_socket)


# передаю клиентский сокет
def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()  # без аргументов кодирует строку в bites
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:

        ready_to_read, _, _ = select(to_monitor,[], []) # read, write, errors

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    #accept_connection(server_socket)
    event_loop()