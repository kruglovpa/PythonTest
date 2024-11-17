# Введение в функциональное программирование
def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__: func(int_list)})
    return results


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))