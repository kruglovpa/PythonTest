class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()
        file.close()

    def add(self, *products):
        katalog = self.get_products()
        for i in products:
            if i.name in katalog:
                print(f'Продукт {i.name} уже есть в каталоге')
            else:
                file = open(self.__file_name, 'a')
                add_prod = f'{str(i)}\n'
                file.write(add_prod)
                file.close()
        self.get_products()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())