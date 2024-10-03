class Car:
    def __init__(self, speed, color, name, is_police: bool) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} едет")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
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
