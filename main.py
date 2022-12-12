#import libraries and modules
import pygame
from pygame.locals import *
import constants
import time
import random

#Creeat the Class Food
class Food():
    def __init__(self, parent_window):
        self.image = pygame.image.load("images\Galleta.png")
        self.parent_window = parent_window
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    #move method
    def move(self):
        self.x = random.randint(40, 950)
        self.y = random.randint(40, 550)        


#Creat the Class dog
class Dog():
    def __init__(self, parent_window, length):
        self.parent_window = parent_window
        self.dog_body = pygame.image.load("images\Dog_body.png")
        self.direction = "right"

        self.length = length
        self.x = [64]*length
        self.y = [64]*length

    def increse_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_window.fill(constants.BG_COLOR)

        for i in range(self.length):

            self.parent_window.blit(self.dog_body, (self.x[i], self.y[i]))
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
        #Update body 
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Update head
        if self.direction == "left":
                self.x[0] -= constants.SIZE_DOG

        if self.direction == "right":
                self.x[0] += constants.SIZE_DOG

        if self.direction == "up":
                self.y[0] -= constants.SIZE_DOG
            
        if self.direction == "dowm":
                self.y[0] += constants.SIZE_DOG

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

        self.dog = Dog(self.window, 3)
        self.dog.draw()

        self.food = Food(self.window)

        self.food.draw()

        pygame.display.update()

    # Collition logic
    def is_collition(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + constants.SIZE_FOOD:
            if y1 >= y2 and y1 < y2 + constants.SIZE_FOOD:
                return True
        return False

    # Play mathod
    def Play(self):
        self.dog.walk()
        self.food.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collition(self.dog.x[0], self.dog.y[0], self.food.x, self.food.y):
            self.dog.increse_length()
            self.food.move()

        # Snake colliding with itself
        for i in range(2, self.dog.length):
            if self.is_collition(self.dog.x[0], self.dog.y[0], self.dog.x[i], self.dog.y[i]):
                print("collition")

    # show score
    def display_score(self):
        font = pygame.font.Font("font.ttf", 60)
        score = font.render(f"Score: {self.dog.length - 3}", True, (255, 255, 255))
        self.window.blit(score, (constants.SCORE_X, constants.SCORE_Y))
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

            self.Play()
            time.sleep(0.2)

game = Game()

game.run()
