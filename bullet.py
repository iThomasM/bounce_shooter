import pygame
from pygame.sprite import Sprite
import math

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.x, self.y = pygame.mouse.get_pos()
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.midtop = game.player.rect.midtop
        x_distance, y_distance = self.x - self.rect.x, self.y - self.rect.y
        length = math.hypot(x_distance, y_distance)
        self.x_dis = x_distance / length
        self.y_dis = y_distance / length

    def update(self):
        self.rect.x += self.x_dis * 10
        self.rect.y += self.y_dis * 10
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect, border_radius=5)

