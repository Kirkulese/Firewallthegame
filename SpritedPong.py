import pygame
import random

pygame.init()

##Define window for display and name it
screenHeight = 500
screenWidth = 1000
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Firewall")

#get the clock ready
clock = pygame.time.Clock()

##create group for all sprites to contain everything
fwSprites = pygame.sprite.Group()

##level modifier
level = 1

##Set FPS
FPS = 30

##color variables
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    ##Create class for basic character paddle
    def __init__(self, color, speed, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)


        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.topleft
        self.speed = speed


    def draw(self, surface):
        #draw image to screen at x,y
        surface.blit(self.image, (self.x, self.y))

    def user_keys(self):
        #create a method for handling user input to clean things up
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            player.y -= player.speed

        if keys[pygame.K_DOWN]:
            player.y += player.speed

#create player
player = Paddle(GREEN, 7, 10, 100)
player.x = 100
##the game's main loop
run = True
while run:
    ##check for input
    for event in pygame.event.get():
        ##quit if window's x is pressed
        if event.type == pygame.QUIT:
            run = False

    if level == 1:


        player.draw(win)
        player.user_keys()

        #update the screen and fill in blank spaces with black
        pygame.display.update()
        win.fill(BLACK)

        #set clock to FPS - specified above
        clock.tick(FPS)

##if run set to false, loop will end and execute quit code
pygame.quit()
