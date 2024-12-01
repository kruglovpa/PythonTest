# Блокировка потоков и обработка ошибок
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            transh = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += transh
            print(f'Пополнение: {transh}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            transh = randint(50, 500)
            print(f'Запрос на {transh}')
            if self.balance >= transh:
                self.balance -= transh
                print(f'Снятие: {transh}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


if __name__ == '__main__':
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
