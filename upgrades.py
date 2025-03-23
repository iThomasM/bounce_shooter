import pygame
from pygame import mixer
import random

class Upgrades:
    def __init__(self, game):
        self.config = game.config
        mixer.init()

        self.screen = game.screen
        self.font = pygame.font.Font("assets/megamax.ttf", 25)
        self.sfx = pygame.mixer.Sound("assets/sfx1.wav")
        self.sfx2 = pygame.mixer.Sound("assets/sfx2.wav")

        self.icon1 = pygame.image.load("assets/icon1.bmp")
        self.icon2 = pygame.image.load("assets/icon2.bmp")
        self.icon3 = pygame.image.load("assets/icon3.bmp")
        self.icon4 = pygame.image.load("assets/icon4.bmp")

        self.rect1 = self.icon1.get_rect()
        self.rect2 = self.icon2.get_rect()
        self.rect3 = self.icon3.get_rect()
        self.rect4 = self.icon4.get_rect()

    def upgrade_menu(self):
        self.icon1_text = self.font.render(f"{self.config.dash_price}$", True, (0, 0, 0))
        self.icon2_text = self.font.render(f"{self.config.bullet_price}$", True, (0, 0, 0))
        self.icon3_text = self.font.render(f"{self.config.speed_price}$", True, (0, 0, 0))
        self.icon4_text = self.font.render(f"{self.config.heal_price}$", True, (0, 0, 0))

        self.rect4.center = 20, 480
        self.rect3.center = 20, 440
        self.rect2.center= 20, 400
        self.rect1.center= 20, 360

        self.screen.blit(self.icon1, self.rect1)
        self.screen.blit(self.icon2, self.rect2)
        self.screen.blit(self.icon3, self.rect3)
        self.screen.blit(self.icon4, self.rect4)

        text1_rect = self.icon1_text.get_rect()
        text1_rect.center = 70, 360
        self.screen.blit(self.icon1_text, text1_rect)

        text2_rect = self.icon2_text.get_rect()
        text2_rect.center = 70, 400
        self.screen.blit(self.icon2_text, text2_rect)

        text3_rect = self.icon3_text.get_rect()
        text3_rect.center = 70, 440
        self.screen.blit(self.icon3_text, text3_rect)

        text4_rect = self.icon4_text.get_rect()
        text4_rect.center = 70, 480
        self.screen.blit(self.icon4_text, text4_rect)

    def click(self, pos):
        if self.rect4.collidepoint(pos):
            self.health_upgrade()
        elif self.rect3.collidepoint(pos):
            self.speed_upgrade()
        elif self.rect2.collidepoint(pos):
            self.bullet_upgrade()
        elif self.rect1.collidepoint(pos):
            self.bounce_upgrade()

    def bounce_upgrade(self):
        if self.config.money - self.config.dash_price >= 0:
            self.config.money -= self.config.dash_price
            self.config.player_dashes += 3
            self.sfx.play()
        else:
            self.sfx2.play()
    
    def speed_upgrade(self):
        if self.config.money - self.config.speed_price >= 0 and self.config.player_speed < 5:
            self.config.money -= self.config.speed_price
            self.config.player_speed += 0.5
            self.config.speed_price += random.randint(5, 6)
            self.sfx.play()
        else:
            self.sfx2.play()

    def bullet_upgrade(self):
        if self.config.money - self.config.bullet_price >= 0 and self.config.bullet_cooldown > 20:
            self.config.money -= self.config.bullet_price
            self.config.bullet_cooldown -= 25
            self.config.bullet_price += 3
            self.sfx.play()
        else:
            self.sfx2.play()

    def health_upgrade(self):
        if self.config.money - self.config.heal_price >= 0:
            self.config.money -= self.config.heal_price
            self.config.player_health = 100
            self.sfx.play()
        else:
            self.sfx2.play()
