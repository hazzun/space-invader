from random import randint

from pygame.sprite import Group

from .base import Enemy
from .explosions import BirdExplosion
from .bullets import BlueSpaceShipBullet, RedSpaceShipBullet, GreenSpaceShipBullet, CircledSpaceShipBullet


class SpaceShip(Enemy):
    COOLDOWN = 100

    def __init__(self, pos_x, pos_y):
        super().__init__('spaceships')
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health_point = 1
        self.explosion = BirdExplosion
        self.weapon = None
        self.weapons = Group()
        self.cool_down_counter = 0

    def update(self, *args, **kwargs) -> None:
        self.cool_down_counter += randint(0, 1)
        self.attack()
        super().update()

    def attack(self) -> None:
        if self.cool_down_counter > self.COOLDOWN:
            self.weapons.add(self.weapon(self.rect.x, self.rect.y))
            self.cool_down_counter = 0


class BlueSpaceShip(SpaceShip):
    # DEFAULT_COUNT = 10
    DEFAULT_COUNT = 1
    COOLDOWN = 70

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 5
        self.set_images('blue_ship')
        self.weapon = BlueSpaceShipBullet
        self.score = 150


class RedSpaceShip(SpaceShip):
    # DEFAULT_COUNT = 10
    DEFAULT_COUNT = 1
    COOLDOWN = 60

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 7
        self.set_images('red_ship')
        self.weapon = RedSpaceShipBullet
        self.score = 200


class GreenSpaceShip(SpaceShip):
    # DEFAULT_COUNT = 15
    DEFAULT_COUNT = 1
    COOLDOWN = 50

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = 8
        self.set_images('green_ship')
        self.weapon = GreenSpaceShipBullet
        self.score = 300


class CircledSpaceShip(SpaceShip):
    DEFAULT_COUNT = 1
    COOLDOWN = 10
    HEALTH_POINT = 20

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.health_point = 20
        self.speed = 8
        self.set_images('circled_ship')
        self.weapon = CircledSpaceShipBullet
        self.score = 1000
        self.health_point = self.HEALTH_POINT
        self.is_boss = True

    def attack(self) -> None:
        if self.cool_down_counter > self.COOLDOWN:
            self.weapons.add(self.weapon(self.rect.x, self.rect.y))
            self.cool_down_counter = 0

    def move(self) -> None:
        if self.rect.x < 0 or 640 - self.image.get_width() < self.rect.x:
            self.speed *= -1
        self.rect.x += self.speed
