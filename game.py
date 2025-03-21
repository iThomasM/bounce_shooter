import pygame
from player import Player
from bullet import Bullet
from enemies import Enemy

class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((500, 500))
        self.running = True
        self.player = Player(self)
        self.max_enemies = 10
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        pygame.display.set_caption("Bounce-Shooter")

    def run_game(self):
        while self.running:
            self._enemy()
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
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
    
    def _shoot(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)

    def _del_bullet(self):
        ...
    
    def _enemy(self):
        enemy = Enemy(self, self.player)
        if len(self.enemies.sprites()) < self.max_enemies:
            self.enemies.add(enemy)

    def _check_keydown(self, event):
        if event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_s:
            self.player.moving_down = True

    def _check_keyup(self, event):
        if event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False

    def _screen(self):
        self.screen.fill((255, 255, 255))
        self.player.draw_player()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for enemy in self.enemies.sprites():
            enemy.spawn()
        pygame.display.flip()
        pygame.display.update()

if __name__ == "__main__":
    game = Main()
    game.run_game()
