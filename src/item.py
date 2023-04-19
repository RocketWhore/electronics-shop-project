import csv


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __str__(self):
        return f'{self.__name} {self.price} {self.quantity}'

    @staticmethod
    def string_to_number(i):
        return int(float(i))

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('../tests/items.csv', 'r') as file:
            data = csv.DictReader(file, delimiter=",")
            print(data)
            for i in data:
                cls(i['name'], i['price'], i['quantity'])

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, __name):
        """Метод срабатывает при операции присваивания."""
        if len(__name) <= 10:
            self.__name = __name


# print(Item.instantiate_from_csv())


print(Item.instantiate_from_csv())
