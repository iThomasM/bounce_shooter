from pygame.sprite import Sprite
import pygame
import math

class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.config = game.config
        self.speed = self.config.player_speed
        self.knockback_int = self.config.player_knockback_duration
        self.dashing_int = self.config.player_dashing_duration
        self.screen_rect = game.screen.get_rect()
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.x_pos = float(screen_width // 2)  
        self.y_pos = float(screen_height // 2)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.sprinting = False
        self.shooting = False
        self.bulletx = 0
        self.bullety = 0
        self.facing = 0
        self.dashing = False

    def draw_player(self):
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 30, 30))
        self.player = pygame.draw.rect(self.screen, (0, 0, 0), self.rect, border_radius=5)

    def update(self):
        if self.sprinting:
            self.speed = self.config.sprint_speed
        else:
            self.speed = self.config.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x_pos -= self.speed
            self.facing = -1
        if self.moving_right and self.rect.right < 500:
            self.x_pos += self.speed
            self.facing = 1
        if self.moving_up and self.rect.top > 0:
            self.y_pos -= self.speed
            self.facing = -2
        if self.moving_down and self.rect.bottom < 500:
            self.y_pos += self.speed
            self.facing = 2
        if self.shooting:
            if self.knockback_int > 0:
                self.kickback(self.bulletx, self.bullety)
                self.knockback_int -= 1
            else:
                self.shooting = False
                self.knockback_int = 5
        if self.dashing:
            if self.dashing_int > 0:
                self.dash()
                self.dashing_int -= 1
            else:
                self.dashing = False
                self.dashing_int = 5

    def dash(self):
        if self.facing == -1 and self.rect.left > 0:
            self.x_pos -= 10
        elif self.facing == 1 and self.rect.right < 500:
            self.x_pos += 10
        elif self.facing == -2 and self.rect.top > 0:
            self.y_pos -= 10
        elif self.facing == 2 and self.rect.bottom < 500:
            self.y_pos += 10

    def kickback(self, x, y):
        if self.rect.left > 0 and self.rect.right < 500:
            self.x_pos -= x * 20
        else:
            self.x_pos += 0
        if self.rect.top > 0 and self.rect.bottom < 500:
            self.y_pos -= y * 20
        else:
            self.y_pos += 0
        
