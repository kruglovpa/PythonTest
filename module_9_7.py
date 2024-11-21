# Дектораторы
def is_prime(func):
    def wrapper(*args):
        my_sum = func(*args)
        sum_true = True
        for i in range(2, my_sum):
            if my_sum % i == 0:
                sum_true = False
                break
        if my_sum != 1 and sum_true:
            return f'Простое \n{my_sum}'
        else:
            return f'Составное\n{my_sum}'

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
