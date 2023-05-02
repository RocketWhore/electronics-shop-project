from src.item import Item

class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        return int(self.quantity) + int(other.quantity)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"
    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim: int):
        if isinstance(new_number_of_sim, int) and new_number_of_sim > 0:
            self.__number_of_sim = new_number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


