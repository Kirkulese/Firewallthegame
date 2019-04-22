import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.win = False

    def new(self):
        # start a new game
        self.message = "Destroy the Firewall to escape!"
        self.message2 = "The red part is vulnerable"
        self.all_sprites = pg.sprite.Group()
        self.ballsprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.upperwall = pg.sprite.Group()
        self.lowerwall = pg.sprite.Group()
        self.bytewall = pg.sprite.Group()



        ##create instances and add them to sprite groups
        self.player = Player(self, 25, HEIGHT / 2)
        self.upperplat = Platform(WIDTH - 150, 125, 20, 125)
        self.lowerplat = Platform(WIDTH - 150, 325, 20, 125)
        self.ball = Ball(WIDTH / 2, HEIGHT / 2, 5, 5)
        self.walls.add(self.upperplat)
        self.walls.add(self.lowerplat)
        self.upperwall.add(self.upperplat)
        self.lowerwall.add(self.lowerplat)
        self.all_sprites.add(self.player)
        self.ballsprite.add(self.ball)
        self.run()

    def level2(self):
        #change messages for level 2
        self.message = "Hack the password by destroying this byte!"
        self.message2 = ""
        self.bytewall = pg.sprite.Group()

        #create instances for level 2
        self.player = Player(self, 25, HEIGHT / 2)
        self.ball = Ball(WIDTH / 3, HEIGHT / 2, 5, 6)
        self.byte = MovingPlatform(WIDTH - 150, 125, 20, 125, 3)
        self.walls.add(self.byte)
        self.all_sprites.add(self.player)
        self.ballsprite.add(self.ball)
        self.bytewall.add(self.byte)
        



    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            if len(self.walls) < 1:
                pg.sprite.Sprite.kill(self.player)
                pg.sprite.Sprite.kill(self.ball)
                self.level2()
            if self.win == True:
                g.show_go_screen()


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.ballsprite.update()
        self.walls.update()

        bncPlayer = pg.sprite.spritecollide(self.ball, self.all_sprites, False)
        bncUWall = pg.sprite.spritecollide(self.ball, self.upperwall, False)
        bncLWall = pg.sprite.spritecollide(self.ball, self.lowerwall, False)
        bncByte = pg.sprite.spritecollide(self.ball, self.bytewall, False)
       

        ##do collisions with walls, first check to see if need to bounce off top and bottom then check sides and destroy if back

        if bncUWall:
            # check edge bounce
            if self.upperplat.rect.top + self.upperplat.h / 13 > self.ball.y or self.ball.y > self.upperplat.rect.bottom - self.upperplat.h / 13:
                self.ball.speedy = -self.ball.speedy
            #or bounce off face
            else:
                self.ball.speedx = -self.ball.speedx
                #check to see if it hits back of wall
                if 860 < self.ball.x < 870 and self.upperplat.rect.top < self.ball.y < self.upperplat.rect.bottom:
                    pg.sprite.Sprite.kill(self.upperplat)
                   

        if bncLWall:
            # check for edge bounces
            if  self.lowerplat.rect.top + self.lowerplat.h / 13 > self.ball.y or self.ball.y > self.lowerplat.rect.bottom - self.lowerplat.h / 13:
                self.ball.speedy = -self.ball.speedy
            # if not bounce off face
            else:
                self.ball.speedx = -self.ball.speedx
                # check to see if it hits back of wall
                if 860 < self.ball.x < 870 and self.lowerplat.rect.top < self.ball.y < self.lowerplat.rect.bottom:
                    pg.sprite.Sprite.kill(self.lowerplat)

        if bncByte:
                # check for edge bounces
                if  self.byte.rect.top + self.byte.h / 10 > self.ball.y or self.ball.y > self.byte.rect.bottom - self.byte.h / 10:
                    self.ball.speedy = -self.ball.speedy
                # if not bounce off face
                else:
                    self.ball.speedx = -self.ball.speedx
                    # check to see if it hits back of wall
                    if 860 < self.ball.x < 870 and self.byte.rect.top < self.ball.y < self.byte.rect.bottom:
                        pg.sprite.Sprite.kill(self.byte)
                        self.win = True
                    
        if bncPlayer:
            self.ball.speedx = -self.ball.speedx

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def draw(self):
        # Game Loop - draww
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.ballsprite.draw(self.screen)
        self.walls.draw(self.screen)
        if len(self.walls) > 0:
            self.draw_text(str(self.message), 22, WHITE, WIDTH / 2, 15)
            self.draw_text(str(self.message2), 22, WHITE, WIDTH / 2, 40)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("You are a sentient bit trying to gain freedom!", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 8)
        self.draw_text("Up and Down to move", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("SWEET SUCCESS!! YOU'VE ESCAPED TO THE INTERNET", 30, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("GOOD LUCK WITH YOUR TRAVELS", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()