class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # название продукта
        self.weight = weight  # общий вес товара
        self.category = category  # категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    # Задание не соответствует примеру работы программы.
    # Задание: добавить продукт в файл, если его названия нет в файле.
    def add(self, *products: Product):
        names = []  # список названий продуктов, содержащихся в файле
        file = open(self.__file_name, 'a+')
        file.seek(0)  # режим 'а' устанавливает курсор на конец файла
        for line in file:
            name = line.split(', ')[0]  # название продукта
            names.append(name)
        for product in products:
            if product.name in names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product}\n')
                names.append(product.name)
        file.close()

    # Добавление продукта согласно примеру работы программы
    # def add(self, *products: Product):
    #     file_products = []  # список продуктов, содержащихся в файле
    #     file = open(self.__file_name, 'a+')
    #     file.seek(0)
    #     for line in file:
    #         file_products.append(line.rstrip())  # без '\n'
    #     for product in products:
    #         if str(product) in file_products:
    #             print(f'Продукт {product} уже есть в магазине')
    #         else:
    #             file.write(f'{product}\n')
    #     file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
