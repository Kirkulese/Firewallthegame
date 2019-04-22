# Sprite classes for platform game
import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((20, 100))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.y -= PLAYER_ACC
        if keys[pg.K_DOWN]:
            self.y += PLAYER_ACC

        self.rect.center = (self.x, self.y)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.right = x + w
        self.rect.top = y
        self.rect.bottom = y + h
        self.h = h
        self.w = w
        
        


class MovingPlatform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, speed):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.right = x + w
        self.rect.top = y
        self.rect.bottom = y + h
        self.rect.left = self.rect.x
        self.speed = speed
        self.h = h

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom > HEIGHT:
            self.speed = -self.speed
        if self.rect.top < 0:
            self.speed = -self.speed

class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.image = pg.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.w = 20


    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y > HEIGHT - 20:
            self.speedy = -self.speedy
        if self.y < 20:
            self.speedy = -self.speedy

        if self.x > WIDTH - 20:
            self.speedx = -self.speedx



