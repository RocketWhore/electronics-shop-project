"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
pay_rate = 0.7

def test_calculate_total_price():
    data = item1.calculate_total_price()

    assert data == item1.price * item1.quantity

def test_apply_discount():
    dats = item1.apply_discount()

    assert dats == None
