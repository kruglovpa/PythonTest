# Позиционирование в файле
def custom_write(file_name, strings):
    num = 1
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')

    for i in strings:
        position = file.tell()
        key = (num, position)
        file.write(f'{i}\n')
        strings_positions.update({key: i})
        num += 1

    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)