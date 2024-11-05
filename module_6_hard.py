# # Дополнительное задание по модулю Наследование классов
from math import pi


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color
        if self.__color:
            self.filled = True
        if isinstance(self.__sides, int):
            self.__sides = [self.__sides] * self.sides_count
        else:
            if len(self.__sides) != self.sides_count:
                self.__sides = [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
                and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return True

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, new_sides):
        for i in new_sides:
            if not isinstance(i, int) or i <= 0:
                return False
                break
        if len(new_sides) != self.sides_count:
            return False
        else:
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    __sides = [0]

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    __sides = [0, 0, 0]

    def get_square(self):
        sides = self.get_sides()
        pp = sum(self.sides) / 2
        return (pp * (pp - sides[0]) * (pp - sides[1]) * (pp - sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12
    # __sides = []

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())