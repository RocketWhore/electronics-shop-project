"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
pay_rate = 0.7


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_string_to_number():
    assert Item.string_to_number('57.354') == 57
    assert Item.string_to_number('9') == 9
    assert Item.string_to_number(181.0) == 181
    # with pytest.raises(ValueError):
    #     assert Item.string_to_number('181.O') == 181


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == '100'
    assert Item.all[0].quantity == '1'


def test_name_setter():
    item = Item('apple', 1.5, 10)
    item.name = 'banana'
    assert item.name == 'banana'


def test_calculate_total_price():
    data = item1.calculate_total_price()

    assert data == item1.price * item1.quantity


def test_apply_discount():
    dats = item1.apply_discount()
    assert dats == None


def test__repr__(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test__str__(item):
    assert str(item) == 'Смартфон'
