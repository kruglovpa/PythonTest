# Генераторные сборки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# print(list(zip(first, second)))
first_result = (len(i[0]) - len(i[1]) for i in zip(first, second) if len(i[0]) != len(i[1]))
# second_result = (len(i[0]) == len(i[1]) for i in zip(first, second))

# print(list(len(i) for i in first), list(len(i) for i in second))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

if __name__ == '__main__':
    print(list(first_result))
    print(list(second_result))
