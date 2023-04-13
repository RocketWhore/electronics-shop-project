
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
        self.name = name
        self.price = price
        self.quantity = quantity


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



item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
# all = [item1, item2]
Item.all.append(item1)
Item.all.append(item2)
print(Item.all)
