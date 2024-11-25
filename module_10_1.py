# Введение в потоки
from time import sleep, time
import threading


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i}\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


if __name__ == '__main__':
    time1 = time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    time2 = time()
    print(f'Работа функций продолжалась {(time2 - time1):.3f} сек.')

    time1 = time()
    thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
    thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
    thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
    thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    time2 = time()
    print(f'Работа потоков продолжалась {(time2 - time1):.3f} сек.')
