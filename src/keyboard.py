from src.item import Item



class MixinLog:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    #
    # def language(self):
    #     if self.language == 'RU' or 'EN':
    #         return self.language
    #     else:
    #         raise ValueError("AttributeError: property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        self.__name = name
        self.__language = 'EN'
# kb = Keyboard('Dark Project KD87A', 9600, 5)
# print(kb.language)
# kb.change_lang()
# print(kb.language)
# kb.language = 'CH'
# print(kb.language)