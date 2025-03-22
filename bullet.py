import pygame
from pygame.sprite import Sprite
import math

class Bullet(Sprite):
    def __init__(self, game, bul_type=None):
        super().__init__()
        self.config = game.config
        self.screen = game.screen
        self.player = game.player
        self.x, self.y = pygame.mouse.get_pos()
        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.midtop = game.player.rect.midtop
        x_distance, y_distance = self.x - self.rect.x, self.y - self.rect.y
        length = math.hypot(x_distance, y_distance)
        self.x_dis = x_distance / length
        self.y_dis = y_distance / length

        if bul_type == 2:
            self.y_dis = self.y_dis / 2

    def update(self):
        self.rect.x += self.x_dis * self.config.bullet_speed
        self.rect.y += self.y_dis * self.config.bullet_speed
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, border_radius=5)
    
    def get_pos(self):
        return self.x_dis, self.y_dis
