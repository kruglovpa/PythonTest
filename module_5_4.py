# Различие атрибутов класса и экземпляра
class House:
    houses_history = []

    def __new__(cls, *args):
        if cls.houses_history is None:
            cls.houses_history = super().__new__(cls)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print('Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other
            return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
