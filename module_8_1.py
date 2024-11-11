# Try и Except
def add_everything_up(a, b):
    try:
        a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return a + b


if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
    print(add_everything_up('яблоко', 'строка'))
