# Дополнительное задание
shifr = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(shifr)):
    kod = []
    for j in range(shifr[i] - 1):
        for k in range(1, shifr[i] - 1):
            if ((numbers[j] + numbers[k]) % shifr[i]) == 0 and numbers[j] != numbers[k] and numbers[j] < numbers[k]:
                kod.append(numbers[j])
                kod.append(numbers[k])
    print(shifr[i], ': ', kod)
