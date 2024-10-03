class Toy:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color


class AnimalToy(Toy):
    def __str__(self):
        return f"Игрушка животного {self.name}, цвет - {self.color}"


class CartoonPersonToy(Toy):
    def __str__(self):
        return f"Игрушка персонажа мультфильма {self.name}, цвет - {self.color}"


class Fabric:
    def __init__(self) -> None:
        pass

    def __purchase_of_raw_materials(self):
        print("Закупка сырья...")
        print("Сырье закуплено.\n")

    def __sewing_toy(self, name):
        print("Пошив игрушки...")
        print(f'Игрушка "{name}" сшита.\n')

    def __coloring_toy(self, color):
        print("Покраска игрушки...")
        print(f"Игрушка окрашена в {color} цвет.\n")

    def create_toy(self, type_of_toy, name, color):
        self.__purchase_of_raw_materials()
        self.__sewing_toy(name)
        self.__coloring_toy(color)
        toy = type_of_toy(name, color)
        print(str(toy) + ", готова!")
        return toy


fabrica = Fabric()
toy = fabrica.create_toy(CartoonPersonToy, "Вуди", "желто-коричневый")
