# David Beazley
# 2015 PyCon
# Concurrency from the Ground up Live

# функции преобразованы в генераторы, где генераторы отдают кортежи,
# где 1й элемент - фильтрующий признак,
# по которому определяется, куда пойдёт сокет, который находится во втором элементе кортежа
# те, куда он пойдет в список на мониторинг за готовностью к чтению
# или за готовностью к записи

import socket # domain: port
from select import select

tasks = [] # список наполняется генераторами


to_read = {} # socket: generator
to_write = {}


def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5001)) #теперь сокет привязан к 5000 порту
    server_socket.listen() #слушает на случай входящих подключений

    while True:

        yield ('read', server_socket)
        # серверный сокет описан серху, теперь время клиентского сокета
        client_socket, addr = server_socket.accept() # read

        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):

    while True:

        yield ('read', client_socket)
        request = client_socket.recv(4096) # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode() # без аргументов кодирует строку в bites
            yield ('write', client_socket)
            client_socket.send(response) # write

    client_socket.close()


def event_loop():

    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock)) # наполняю список генераторами по значению ключа sock

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock)) # наполняю список генераторами по значению ключа sock

        try:
            task = tasks.pop(0) # 1 elem, task = generator

            reason, sock = next(task) # ('write', client_socket)
            if reason == 'read': # в словаре создается пара
                to_read[sock] = task

            if reason == 'write':  # в словаре создается пара
                to_read[sock] = task

        except StopIteration:
            print('Done')


tasks.append(server())
event_loop()
