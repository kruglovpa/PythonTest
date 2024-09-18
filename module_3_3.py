# Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

value_list = [2, 'строка', True]
value_dict = {'a': 1, 'b': 'строка', 'c': True}
value_list2 = [54.32, 'Строка']

print_params(*value_list2, 42)
