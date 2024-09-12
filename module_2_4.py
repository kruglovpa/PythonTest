# Цикл for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    is_prime = True
    for j in range(1, i):
        if numbers[i] // numbers[j] > 1 and numbers[i] % numbers[j] == 0:
            is_prime = False
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append (numbers[i])
print('Простые числа:', primes)
print('Составные числа:', not_primes)
