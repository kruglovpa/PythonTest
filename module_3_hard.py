# Дополнительное задание
calc_all = 0


def calc_string(i):
    global calc_all
    if type(i) == int:
        calc_all += i
    elif type(i) == str:
        calc_all += len(i)


def calculate_structure_sum(data_structure):
    for i in data_structure:
        if not isinstance(i, str) and not isinstance(i, int) and not isinstance(i, dict):
             calculate_structure_sum(i)
        elif isinstance(i, dict):
             calculate_structure_sum(i.keys())
             calculate_structure_sum(i.values())
        else:
            calc_string(i)
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
