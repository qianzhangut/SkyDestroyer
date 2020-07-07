import random
import pygame as pg

# screen size
SCREEN_RECT = pg.Rect(0,0,480,700)
# Frame rate
FRAME_PER_SEC = 60
# define timer variale
CREAT_ENEMY_EVENT = pg.USEREVENT
# hero fire in the hole
HERO_FIRE_EVENT = pg.USEREVENT + 1
#
SCORE = 0


class GameSprite(pg.sprite.Sprite):
    """SkyDestoryer game sprite"""

    def __init__(self, image_name, speed=1):
        # parent class init
        super().__init__()

        self.image = pg.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # move vertically
        self.rect.y += self.speed


class Background(GameSprite):
    """game backgroud sprite"""
    def __init__(self, is_alt=False):
        # 1. use parent class to creat sprite
        super().__init__("./images/background.png")
        # 2. check if alternate image
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1. Use parent class
        super(Background, self).update()

        # 2. Check if backgroud is out, if so, let move backgroup to the top is screen
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """Enemy sprites"""

    def __init__(self):
        # 1. creat enemy sprite from parent
        super().__init__("./images/enemy1.png")
        # 2. give initial random speed 1-3
        self.speed = random.randint(1, 3)
        # 3. give inital location
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1. vertically fly from parent
        super().update()
        # 2. if out screen, delete from sprites groups
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        #print("enemy crashed %s"% self.rect)
        pass


class Hero(GameSprite):
    """Hero sprites and groups"""

    def __init__(self):
        # 1. use parent class method
        super(Hero, self).__init__("./images/me1.png", 0)

        # 2. inital location
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # creat bullet sprite groups
        self.bullets = pg.sprite.Group()

    def update(self):
        # 1. hero moves horizontally
        self.rect.x += self.speed

        # control hero not out
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 1. creat bullet sprites
        for i in range(3):
            bullet = Bullet()
            # 2. sprites loc
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            # 3. add to groups
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """Enemy sprites"""

    def __init__(self):
        # 1. creat bullet sprite from parent
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 1. vertically fly from parent
        super().update()
        # 2. if out screen, delete from sprites groups
        if self.rect.bottom <0:
            self.kill()

    def __del__(self):
        #print("enemy crashed %s"% self.rect)
        pass

