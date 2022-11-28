#import libraries and modules
import pygame
from pygame.locals import *
import constants
import time

#Creat the Class dog
class Dog():
    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.dog_body = pygame.image.load("images\Dog_body.png")
        self.x = 200
        self.y = 100
        self.direction = "right"

    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)
        self.parent_window.blit(self.dog_body, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):   
        self.direction = "left"

    def move_right(self):   
        self.direction = "right"

    def move_up(self):   
        self.direction = "up"

    def move_dowm(self):   
        self.direction = "dowm"

    def walk(self):
        if self.direction == "left":
            self.x -= 10

        if self.direction == "right":
            self.x += 10

        if self.direction == "up":
            self.y -= 10
        
        if self.direction == "dowm":
            self.y += 10

        self.draw()


#Creat the Class game
class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(constants.SIZE)
        self.title = pygame.display.set_caption(constants.TITLE)
        self.window.fill(constants.BG_COLOR)
        icon = pygame.image.load("images\icon.png")
        pygame.display.set_icon(icon)

        self.dog = Dog(self.window)
        self.dog.draw()

        pygame.display.update()
        
#       
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.dog.move_left()
    
                    if event.key == K_RIGHT:
                        self.dog.move_right()

                    if event.key == K_UP:
                        self.dog.move_up()

                    if event.key == K_DOWN:
                        self.dog.move_dowm()

                elif event.type == QUIT:
                    running = False

            self.dog.walk()     
            time.sleep(.1)

game = Game()

game.run()
