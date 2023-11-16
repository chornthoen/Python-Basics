def say():
    print('Hello World')


def sayHello(name):
    print('Hello ' + name)


def add(x, y):
    print(x + y)
    return x + y


def tuple_return(x, y):
    print(x + y, x - y, x * y, x / y)
    return x + y, x - y, x * y, x / y


def tuple_string(*args):
    print(args)
    print(type(args))
    for arg in args:
        print(arg)


def multi_name(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


say()
sayHello('Dara')
add(1, 2)
tuple_return(1, 2)
tuple_string('Dara', 'Sok', 'Heng', 'Chan', 'Kong')
multi_name(name='Dara', age=24, is_married=False)
