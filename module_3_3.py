# Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

value_list = [2, 'строка', True]
value_dict = {'a': 1, 'b': 'строка', 'c': True}
value_list2 = [54.32, 'Строка']

print_params()
print_params(5)
print_params(5, 8)
print_params(False, 5, 'проверка')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list2)
print_params(*value_list2, 42)
