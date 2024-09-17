# Пространство имен
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    string2 = tuple([len(string), string.upper(), string.lower()])
    count_calls()
    return (string2)


def is_contains(string, list_to_search):
    lower_list = []
    for i in list_to_search:
        i = i.lower()
        lower_list.append(i)
    contains = (string.lower() in lower_list)
    count_calls()
    return (contains)
    

print(string_info('Capybara'))
print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
