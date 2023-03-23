import pygame
import random


class Human:
    def __init__(self, rect, image, x, y):
        self.width = rect.w
        self.height = rect.h
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.size = (70, 80)
        self.rect = pygame.Rect(self.pos, self.size)
        self.move_x = random.randint(-1, 1)
        self.move_y = random.randint(-1, 1)
        self.score = 1000
        self.move_count = 0
        self.sprite_list = [pygame.image.load("Sprites/Dad/Dad_Walk_Up-1.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Up-2.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Down-1.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Down-2.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Left-1.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Left-2.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Right-1.png"),
                            pygame.image.load("Sprites/Dad/Dad_Walk_Right-2.png")]

    def spawn(self):
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
        pygame.screen.blit(self.rect)

    def move(self):
        self.x += self.move_x
        self.y += self.move_y
        self.move_count += 1

        if self.move_x == 1 and self.move_y == 1:
            while True:
                self.image = self.sprite_list[6]
                self.image = self.sprite_list[7]

        if self.move_x == -1 and self.move_y == 1:
            while True:
                self.image = self.sprite_list[4]
                self.image = self.sprite_list[5]

        if self.move_x == 0 and self.move_y == 1:
            self.image = self.sprite_list[2]
            self.image = self.sprite_list[3]

        if self.move_x == 1 and self.move_y == -1:
            while True:
                self.image = self.sprite_list[6]
                self.image = self.sprite_list[7]

        if self.move_x == -1 and self.move_y == -1:
            while True:
                self.image = self.sprite_list[4]
                self.image = self.sprite_list[5]

        if self.move_x == 0 and self.move_y == -1:
            while True:
                self.image = self.sprite_list[0]
                self.image = self.sprite_list[1]

        if self.move_x == 1 and self.move_y == 0:
            while True:
                self.image = self.sprite_list[6]
                self.image = self.sprite_list[7]

        if self.move_x == -1 and self.move_y == 0:
            while True:
                self.image = self.sprite_list[4]
                self.image = self.sprite_list[5]

    def change_walk(self):
        if self.move_count == 30:
            self.move_x = random.randint(-1, 1)
            self.move_y = random.randint(-1, 1)

            if self.move_x == 0 and self.move_y == 0:
                self.move_x = random.randint(-1, 1)
                self.move_y = random.randint(-1, 1)

   # def score_up(self):
        #A cada huamno resgatado
            #if self.score >= 5000:
                #self.score += 1000
