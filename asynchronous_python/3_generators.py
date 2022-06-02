# можно поставить выполнение функции на паузу
from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000) # unix time в мили секунды
        yield pattern.format(str(t))


def gen(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen('olya')
g2 = gen2(4)

task = [g1, g2]

while task:
    tsk = task.pop(0)

    try:
        i = next(tsk)
        print(i)
        task.append(tsk)
    except StopIteration:
        pass

