# Потоки на классах
import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.wars = 100
        self.count = 0

    def run(self):
        print(f'{self.name}, на нас напали')
        while self.wars > 0:
            self.wars -= self.power
            sleep(1)
            self.count += 1
            print(f'{self.name} сражается {self.count} дней, осталось {self.wars} воинов')
        print(f'{self.name} одержал победу спустя {self.count} дней')


if __name__ == "__main__":
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)
    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    # Вывод строки об окончании сражения
    print(f'Сражение закончено')
