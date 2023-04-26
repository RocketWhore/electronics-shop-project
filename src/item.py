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
        return f'{self.__name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    @staticmethod
    def string_to_number(i):
        return int(float(i))

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('../tests/items.csv', 'r') as file:
            data = csv.DictReader(file, delimiter=",")

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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
                """
        global_price = self.quantity * self.price
        return global_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    # print(Item.instantiate_from_csv())


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
# all = [item1, item2]
Item.all.append(item1)
Item.all.append(item2)
# print(Item.all)
