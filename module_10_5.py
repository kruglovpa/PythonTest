# Многопроцессорное программирование
from multiprocessing import Pool
from time import time


def read_info(name):
    all_data = []
    file = open(name, 'r')
    for line in file:
        if len(line):
            all_data.append(line)
    file.close


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]
    time_1 = time()
    for file in filenames:
        read_info(file)
    time_2 = time()
    print(f'Линейное время {time_2 - time_1}')

    filenames = [f'file {number}.txt' for number in range(1, 5)]
    time_1 = time()
    with Pool() as pool:
        result = pool.map(read_info, filenames)
    time_2 = time()
    print(f'Многопроцессорное время  {time_2 - time_1}')
