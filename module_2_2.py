# Условная конструкция
first = input ('Введите первое число: ')
second = input ('Введите второе число: ')
third = input ('Введите третье число: ')
if first == second == third :
    print ('Одинаковых чисел 3')
elif first == second or second == third or first == third :
    print ('Одинаковых чисел 2')
else :
    print ('Одинаковых чисел 0')
