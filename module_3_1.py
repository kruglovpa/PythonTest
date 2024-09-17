# Пространство имен
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    print(tuple([len(string), string.upper(), string.lower()]))
    count_calls()


def is_contains(string, list_to_search):
    lower_list = []
    for i in list_to_search:
        i = i.lower()
        lower_list.append(i)
    print(string.lower() in lower_list)
    count_calls()


string_info('Capybara')
string_info('Armageddon')

is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])

print(calls)
