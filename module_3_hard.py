# Дополнительное задание
calc_all = 0


def calc_string(i):
    global calc_all
    for j in i:
        if type(j) == int:
            calc_all += j
        elif type(j) == str:
            calc_all += len(j)


def calculate_structure_sum(data_structure):
    for i in data_structure:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, str):
             calc_string(i)
        elif isinstance(i, dict):
             calc_string(i.keys())
             calc_string(i.values())
        else:
            calculate_structure_sum(i)
    return calc_all


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
