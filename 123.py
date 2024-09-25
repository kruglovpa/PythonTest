new_structure = []

def structure(data_structure):
    for i in data_structure:
        if not isinstance(i, str) and not isinstance(i, int) and not isinstance(i, dict):
            structure(i)
        elif isinstance(i, dict):
            structure(i.keys())
            structure(i.values())
        else:
            new_structure.append(i)
    return new_structure


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

primer = structure(data_structure)
print(primer)
