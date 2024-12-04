# Очереди в потоках
from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                free = True
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел за стол {table.number}')
                    free = False
                    break
            if free:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or (table.guest for table in tables):
            print(guests)
            for table in tables:
                sleep(1)
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал и ушел. Стол номер {table.number} свободен.')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел из очереди и сел за стол {table.number}')
                        table.guest.start()


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = ['Мария', 'Олег', 'Александра', 'Сергей', 'Дарья',
                    'Виктория', 'Никита', 'Галина', 'Павел', 'Илья']
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
