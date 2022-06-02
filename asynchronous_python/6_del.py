# делегирующий генератор
# подгенератор

def coroutine(func):
    # инициализация генератора
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    # генератор что-то читает
    while True:
        try:
            message = yield
        except StopIteration:

            break
        else:
            print('....', message)

    return 'Returned from subgen()'


@coroutine
def delegator(g):
    # генератор что-то транслирует
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g   # передача данных в подгенератор
    print(result)
