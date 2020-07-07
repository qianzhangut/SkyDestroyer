import pygame as pg
from plane_sprite import *


class SkyDestroyer(object):
    """Sky Destroyer main game"""
    def __init__(self):
        # print("Initializing Game")
        # 1. Creat game window
        self.screen = pg.display.set_mode(SCREEN_RECT.size)
        # 2. Creat game clock
        self.clock = pg.time.Clock()
        # 3. Creat sprite and sprite groups
        self.__creat_sprites()
        # 4. set timer event -> enemy 1s
        pg.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        pg.time.set_timer(HERO_FIRE_EVENT, 500)
        # 5. record score
        self.score = SCORE

    def __creat_sprites(self):
        # creat backgroup sprite and groups
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pg.sprite.Group(bg1, bg2)
        # creat enemy sprite and groups
        self.enemy_group = pg.sprite.Group()
        # creat hero sprite and groups
        self.hero = Hero()
        self.hero_group = pg.sprite.Group(self.hero)

    def start_game(self):
        # print("Game Start")

        while True:
            # 1. Set clock rate
            self.clock.tick(FRAME_PER_SEC)
            # 2. Listen event
            self.__event_handler()
            # 3. collision check
            self.__check_collide()
            # 4. update/plot sprites
            self.__update_sprites()
            # 5. update plot
            pg.display.update()

    def __event_handler(self):
        for event in pg.event.get():
            # check if quit game
            if event.type == pg.QUIT:
                SkyDestroyer.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                #print("enemy appear")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            #     print("move right")
        # return all pressed keys tuple, if one key is pressed, it is 1
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_RIGHT]:
            #print("move right")
            self.hero.speed = 3
        elif keys_pressed[pg.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 1. bullet destroy enemy
        kills = pg.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        if len(kills) > 0:
            self.score += 1
        # 2. enemy destroy hero
        enemies = pg.sprite.spritecollide(self.hero, self.enemy_group, True)
        # check if list is empty
        if len(enemies) > 0:
            # let hero die
            self.hero.kill()
            print("You have destroyed %s enemies. Good Job!" % self.score)
            SkyDestroyer.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game Over")

        pg.quit()
        exit()


if __name__ == '__main__':

    # creat game object
    game = SkyDestroyer()

    game.start_game()