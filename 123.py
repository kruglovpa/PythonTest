new_structure = []
def structure (data_structure):
    for i in data_structure:
        if isinstance(i, str) or isinstance(i, int):
            new_structure.append(i)
        else:
            return structure (i)

    return new_structure


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

primer = structure (data_structure)
print(f'Old: {data_structure}')
print(f'New: {primer}')
