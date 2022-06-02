# регистрирую сокеты вместе с сопровождающими данными
# в event_loop кортеж используется "контейнер" для хранения нужных данных

import socket # domain: port
import selectors

selector = selectors.DefaultSelector()


def server():
    # создаю серверный сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5001)) #теперь сокет привязан к 5000 порту
    server_socket.listen() #слушает на случай входящих подключений

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


# передаю в функцию, где создаю клиентский сокет
def accept_connection(server_socket):
    # серверный сокет описан серху, теперь время клиентского сокета
    client_socket, addr = server_socket.accept() # читает данные из входящего буфера
    print('Connection from', addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


# передаю клиентский сокет
def send_message(client_socket):

    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()  # без аргументов кодирует строку в bites
        client_socket.send(response)
    else:
        selector.unregister(client_socket) # снимаю с регистрации
        client_socket.close()


def event_loop():
    while True:

        events = selector.select() #  список таких кортежей (key, events)

        # Selectorkey = ()
        # fileobj
        # events
        # data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
