import pygame
from pygame.sprite import Sprite
import random
import math

class Enemy(Sprite):
    def __init__(self, game, player):
        super().__init__()
        self.screen = game.screen
        self.player = player
        self.playerx = player.x_pos
        self.playery = player.y_pos
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        
        
    def spawn(self):
        self.enemy = pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
    
    @property
    def goto(self, player):
        self.playerx = player.x_pos
        self.playery = player.y_pos
    
    @goto.setter
    def goto(self, player):
        self.playerx = player.x_pos
        self.playery = player.y_pos

    def get_distance(self):
        x_distance, y_distance = self.x - self.playerx, self.y - self.playery
        length = math.hypot(x_distance, y_distance)
        self.x_dis = x_distance / length
        self.y_dis = y_distance / length
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        self.get_distance()
        self.goto = self.player
        
        self.rect.x -= self.x_dis 
        self.rect.y -= self.y_dis