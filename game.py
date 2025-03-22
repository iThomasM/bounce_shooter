import pygame
from player import Player
from bullet import Bullet
from enemies import Enemy
from config import Config

class Main:
    def __init__(self):
        pygame.init()
        self.config = Config()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.config.screen_width, self.config.screen_height))
        self.running = True
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        pygame.display.set_caption("Bounce-Shooter")

    def run_game(self):
        while self.running:
            self._enemy_fleet()
            self._del_bullet()
            self._check_events()
            self._screen()
            self.enemies.update()
            self.enemies.goto = self.player
            self.bullets.update()
            self.player.update()
            self.clock.tick(60)
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._shoot()
                self.player.shooting = True
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
            self.player.dashing = True

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
        bullet = Bullet(self)
        bullet2 = Bullet(self, bul_type=2)
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
        pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

    def _enemy_fleet(self):
        enemy = Enemy(self, self.player)
        if len(self.enemies.sprites()) < self.config.max_enemies:
            self.enemies.add(enemy)

    def _screen(self):
        self.bg = pygame.image.load("bg.bmp")
        self.bg = pygame.transform.scale(self.bg, (500, 500))
        self.screen.blit(self.bg, (0, 0))
        self.player.draw_player()
        self._render_bullets()
        self._render_enemies()
        pygame.display.flip()
        pygame.display.update()
    
    def _render_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
    def _render_enemies(self):
        for enemy in self.enemies.sprites():
            enemy.spawn()
            if not enemy.get_distance():
                self.enemies.remove(enemy)

if __name__ == "__main__":
    game = Main()
    game.run_game()
