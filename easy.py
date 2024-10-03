class Car:
    def __init__(self, speed, color, name, is_police: bool = False) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} едет")

    def stop(self):
        print(f"{self.name} остановился")

    def turn(self, direction: str):
        print(f"{self.name} поворачивает {direction}")


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool = True) -> None:
        super().__init__(speed, color, name, is_police)


lamba = SportCar(
    300,
    "желтый",
    "Ламборгини",
)
lamba.go()
lamba.turn("налево")
lamba.stop()
