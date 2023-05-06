
from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_str():
    assert str(kb) == 'Dark Project KD87A'

def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == 'RU'
