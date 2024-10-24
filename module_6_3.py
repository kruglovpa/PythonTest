# Множественное наследование
class Horse:
    def __ini__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        x_distance += dx
        return x_distance


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        y_distance += dy
        return y_distance

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super.run()
        super.fly()

    def get_pos(self):
        distance = [super.x_distance, super.y_distance]
        return distance

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()