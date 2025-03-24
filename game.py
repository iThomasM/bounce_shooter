import pygame
from player import Player
from bullet import Bullet
from enemies import Enemy
from config import Config
from pygame.locals import *
from pygame import mixer
from gameover import GameOver
from upgrades import Upgrades
import random

class Main:
    def __init__(self):
        mixer.init()
        pygame.init()
        #Music and SFX
        self.music = mixer.Sound("assets/thing.wav")
        self.music.set_volume(0.3)
        self.music.play()
        #Basic Setup
        self.config = Config()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.config.screen_width, self.config.screen_height))
        self.running = False
        self.menu = True
        self.bg = pygame.image.load("assets/bg.bmp")
        self.bg = pygame.transform.scale(self.bg, (self.config.screen_width, self.config.screen_height))
        #Everything else
        self.player = Player(self)
        self.upgrades = Upgrades(self)
        self.bullet_cooldown = self.config.bullet_cooldown
        self.alive = True
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        pygame.display.set_caption("Bounce-Shooter")
        self.font = pygame.font.Font("assets/megamax.ttf", 90)
        self.menu_text = self.font.render("PLAY", True, (255, 150, 255))
        
        while self.menu:
            pos = pygame.mouse.get_pos()
            self.bg = pygame.image.load("assets/bg.bmp")
            self.bg = pygame.transform.scale(self.bg, (500, 500))
            self.screen.blit(self.bg, (0, 0))
            text_rect = self.menu_text.get_rect()
            text_rect.center = (250, 250)
            self.screen.blit(self.menu_text, text_rect)
            pygame.display.flip()
            pygame.display.update()
            if text_rect.collidepoint(pos):
                self.menu_text = self.font.render("PLAY", True, (255, 0, 255))
            else:
                self.menu_text = self.font.render("PLAY", True, (255, 150, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_rect.collidepoint(pos):
                        self.running = True
                        self.run_game()

    def run_game(self):
        self.menu = False
        self.music.stop()
        while self.running:
            if not self.alive:
                GameOver(self, self.config)
            self._enemy_fleet()
            self._del_bullet()
            self._check_events()
            self._screen()
            self._player_damage()
            self._bul_cooldown()
            self._bullet_collide()
            self.enemies.update()
            self.enemies.goto = self.player
            self.bullets.update()
            self.player.update()
            self.clock.tick(60)
        
    def _check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self._bul_cooldown():
                    self._shoot()
                    self.player.shooting = True
                self.upgrades.click(pos)
                if self.player.shooting:
                    self.bullet_cooldown = self.config.bullet_cooldown
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
    
    def _check_keydown(self, event):
        if event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_s:
            self.player.moving_down = True
        elif event.key == pygame.K_LSHIFT:
            self.player.sprinting = True
        elif event.key == pygame.K_SPACE:
            if self.config.player_dashes != 0:
                self.player.dashing = True
                self.config.player_dashes -= 1

    def _check_keyup(self, event):
        if event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False
        elif event.key == pygame.K_LSHIFT:
            self.player.sprinting = False

    def _shoot(self):
        if self._bul_cooldown():
            bullet = Bullet(self)
            bullet2 = Bullet(self, bul_type=2)
            if self.config.bullet_cooldown <= 60:
                bullet3 = Bullet(self, bul_type=3)
                self.bullets.add(bullet3)
                self.config.player_knockback_amount = 16
                if self.config.bullet_cooldown <= 30:
                    self.config.player_knockback_amount = 12
            self.bullets.add(bullet)
            self.bullets.add(bullet2)
            self.player.bulletx = bullet.x_dis
            self.player.bullety = bullet.y_dis

    def _del_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
            elif bullet.rect.top > 500:
                self.bullets.remove(bullet)
            elif bullet.rect.left < 0:
                self.bullets.remove(bullet)
            elif bullet.rect.right > 500:
                self.bullets.remove(bullet)

    def _bullet_collide(self):
        if pygame.sprite.groupcollide(self.bullets, self.enemies, True, True):
            self.config.score += 1
            self.config.money += random.randint(1, 3)
            if self.config.max_enemies < 10:
                self.config.max_enemies += 0.2

    def _enemy_fleet(self):
        enemy = Enemy(self, self.player)
        if len(self.enemies.sprites()) < self.config.max_enemies:
            self.enemies.add(enemy)

    def _render_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
    def _render_enemies(self):
        for enemy in self.enemies.sprites():
            enemy.spawn()
            if not enemy.get_distance():
                self.enemies.remove(enemy)

    def _killcount(self):
        font = pygame.font.Font("assets/megamax.ttf", 25)
        text = font.render(f"Kills: {self.config.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        self.screen.blit(text, text_rect)

    def _moneycount(self):
        font = pygame.font.Font("assets/megamax.ttf", 25)
        text = font.render(f"${self.config.money}", True, (0, 0, 0))
        money_rect = text.get_rect()
        money_rect.topleft = (10, 70)
        self.screen.blit(text, money_rect)
    
    def _stats(self):
        font = pygame.font.Font("assets/megamax.ttf", 25)
        text = font.render(f"Dash: {self.config.player_dashes}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 40)
        self.screen.blit(text, text_rect)

    def _healthbar(self):
        font = pygame.font.Font("assets/megamax.ttf", 25)
        text = font.render(f"HP: {self.config.player_health}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topright = (490, 10)
        self.screen.blit(text, text_rect)
    
    def _player_damage(self):
        if pygame.sprite.groupcollide(self.sprites, self.enemies, False, True):
            self.config.player_health -= random.randint(10, 27)
        if self.config.player_health <= 0:
            self.alive = False

    def _bul_cooldown(self):
        if self.bullet_cooldown != 0:
            self.bullet_cooldown -= 1
        else:
            return True
        
    def _screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.player.draw_player()
        self._render_bullets()
        self._render_enemies()
        self._killcount()
        self._healthbar()
        self._moneycount()
        self._stats()
        self.upgrades.upgrade_menu()
        pygame.display.flip()
        pygame.display.update()
        
if __name__ == "__main__":
    game = Main()