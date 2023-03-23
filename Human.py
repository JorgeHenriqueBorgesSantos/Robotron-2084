import pygame
import random
import time

class Human:
    def __init__(self, rect, image, x, y, score):
        self.width = rect.w
        self.height = rect.h
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = x
        self.y = y
        self.move_x = random.randint(-1, 1)
        self.move_y = random.randint(-1, 1)
        self.score = 1000
        self.move_count = 0

    def spawn(self):
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
        pygame.screen.blit(self.rect)

    def move(self):
        self.x += self.move_x
        self.y += self.move_y
        self.move_count += 1

    def change_walk(self):
        if self.move_count == 30:
            self.move_x = random.randint(-1, 1)
            self.move_y = random.randint(-1, 1)

   # def score_up(self):
        #A cada huamno resgatado
            #if self.score >= 5000:
                #self.score += 1000
