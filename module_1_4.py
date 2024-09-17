# организация программ и методы строк
my_string = input('Введите любой текст ')
count = len(my_string)
print('В вашем тесте ', int(count), 'символов')
print('ваш текст в верхнем регистре: ', my_string.upper())
print('ваш текст в нижнем регистре: ', my_string.lower())
print('ваш текст без пробелов: ', my_string.replace(' ', ''))
print('первый символ строки ', my_string[0])
print('последний символ строки ', my_string[-1])
