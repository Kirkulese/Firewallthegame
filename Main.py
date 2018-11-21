import pygame
import random

pygame.init()

##Define window for display and name it

screenHeight = 500
screenWidth = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Firewall")

##create group for all sprites to contain everything
fwSprites = pygame.sprite.Group()

##level modifier
level = 1

##color variables
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

##create class for character
class paddle(object):
    def __init__(self, x, y, width, height, health, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed

##class for level 1 walls, they have a front and a back. if it hits the back it will get destroyed
class level1paddle(object):
    def __init__(self, x, y, frontWidth, frontHeight, backWidth, backHeight, health):
        self.x = x
        self.y = y
        self.frontWidth = frontWidth
        self.frontHeight = frontHeight
        self.backWidth = backWidth
        self.backHeight = backHeight
        self.health = health

##class for the ball object needs a radius
class ball(object):
    def __init__(self, x, y, radius, speedx, speedy):
        self.x = x
        self.y = y
        self.radius = radius
        self.speedx = speedx
        self.speedy = speedy

    def move(self):
        ##collide with vertical boundaries
        if self.y > screenHeight - self.radius - 10:
            self.speedy = self.speedy*-1
        elif self.y < self.radius + 10:
            self.speedy = self.speedy * -1


        ##collide with level walls
        if self.x == topWall.x and topWall.y < self.y < topWall.y + topWall.frontHeight:
            self.speedx = self.speedx * -1
        elif self.x == midWall.x and midWall.y < self.y < midWall.y + midWall.frontHeight:
            self.speedx = self.speedx * -1
        elif self.x == botWall.x and botWall.y < self.y < botWall.y + botWall.frontHeight:
            self.speedx = self.speedx * -1

        ##collide with player paddle
        if self.x - self.radius <= player.x + player.width and player.y <= self.y <= player.y + player.height:
            self.speedx = self.speedx * -1

        ##set initial movement
        self.x += self.speedx * -1
        self.y += self.speedy
##create player
player = paddle(150, 220, 10, 100, 100, 15)

##create basic ball

basicBall = ball(500, 225, 8, 10, 8)

##the game's main loop
run = True
while run:
    ##this is the "lag" so things dont happen too quickly in milliseconds
    pygame.time.delay(40)

    ##check for input
    for event in pygame.event.get():
        ##quit if window's x is pressed
        if event.type == pygame.QUIT:
            run = False

    ##shortcut for keypresses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player.speed

    if keys[pygame.K_DOWN] and player.y < 450:
        player.y += player.speed

    win.fill((0,0,0))
    if level == 1:
        ##create walls for level 1
        topWall = level1paddle(850, 50, 10, 100, 5, 100, 1)
        midWall = level1paddle(850, 200, 10, 100, 5, 100, 1)
        botWall = level1paddle(850, 350, 10, 100, 5, 100, 1)


        ##draw rectangle to be played
        pygame.draw.rect(win, (0,255,0), (player.x, player.y, player.width, player.height))

        ##move ball
        basicBall.move()

        ##draw ball
        pygame.draw.circle(win, (0, 255,0), (basicBall.x, basicBall.y), basicBall.radius, 0)

        ##draw firewalls
        pygame.draw.rect(win, (0, 255, 0), (topWall.x, topWall.y, topWall.frontWidth, topWall.frontHeight))
        pygame.draw.rect(win, (255, 0, 0), (topWall.frontWidth + topWall.x, topWall.y, topWall.backWidth, topWall.backHeight))
        pygame.draw.rect(win, (0, 255, 0), (midWall.x, midWall.y, midWall.frontWidth, midWall.frontHeight))
        pygame.draw.rect(win, (255, 0, 0), (midWall.frontWidth + midWall.x, midWall.y, midWall.backWidth, midWall.backHeight))
        pygame.draw.rect(win, (0, 255, 0), (botWall.x, botWall.y, botWall.frontWidth, botWall.frontHeight))
        pygame.draw.rect(win, (255, 0, 0), (botWall.frontWidth + botWall.x, botWall.y, botWall.backWidth, botWall.backHeight))

        #draw bounding walls
        pygame.draw.rect(win, (0, 255, 0), (100, 5, 800, 5))
        pygame.draw.rect(win, (0, 255, 0), (100, 490, 800, 5))
        ##refresh the game to display things drawn
        pygame.display.update()

##if run set to false, loop will end and execute quit code
pygame.quit()


