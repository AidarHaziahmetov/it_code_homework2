import random


class Person:
    def __init__(self, health, damage, armor) -> None:
        self.__health = health
        self.__damage = damage
        self.__armor = armor

    def __calculate_received_damage(self, damage):
        received_damage = damage - self.__armor
        if self.__armor >= damage:
            return 0
        if self.__health - received_damage < 0:
            return self.__health
        return received_damage

    def take_damage(self, damage):
        self.__health -= self.__calculate_received_damage(damage)

    def attack(self, target):
        target.take_damage(self.__damage)

    def is_live(self):
        if self.__health <= 0:
            return False
        return True


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:
    def __init__(self, player_stats=(100, 15, 5), enemy_stats=(100, 10, 10)) -> None:
        self.player = Player(*player_stats)
        self.enemy = Enemy(*enemy_stats)
        self.turn_to_walk = random.choice(("player", "enemy"))

    def game_cycle(self):
        while self.player.is_live() and self.enemy.is_live():
            if self.turn_to_walk == "player":
                who_attack = self.player
                target = self.enemy
                self.turn_to_walk = "enemy"
            else:
                who_attack = self.enemy
                target = self.player
                self.turn_to_walk = "player"
            who_attack.attack(target)
        if self.player.is_live():
            print("player win")
        else:
            print("enemy win")


game = Game()
game.game_cycle()
