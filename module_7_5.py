# Файлы в операционной системе
import os
import time

directory = os.getcwd()
# files = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(files)
# print(dirs)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
