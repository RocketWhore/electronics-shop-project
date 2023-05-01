import pytest

from src.phone import Phone

iphone = Phone("iPhone 14", 120_000, 5, 2)


def test_str():
    assert str(iphone) == "iPhone 14"


def test_add():
    assert iphone + iphone == 10

def test_number_of_sim():
    with pytest.raises(ValueError):
        iphone.number_of_sim = 'new sim'
    # assert iphone.number_of_sim == 2



