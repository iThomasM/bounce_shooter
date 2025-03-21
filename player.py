from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.x_pos = float(screen_width // 2)  
        self.y_pos = float(screen_height // 2)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 2

    def draw_player(self):
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 30, 30))
        self.player = pygame.draw.rect(self.screen, (0, 0, 0), self.rect, border_radius=5)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.speed
        if self.moving_right and self.rect.right < 500:
            self.x_pos += self.speed
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.speed
        if self.moving_down and self.rect.bottom < 500:
            self.y_pos += self.speed
