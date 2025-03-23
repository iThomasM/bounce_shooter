import pygame
import json

class GameOver:
    def __init__(self, game, config):
        self.game = game
        self.alive = game.alive
        self.score = config.score

        with open("score.json", "r+") as f:
            data = json.load(f)
        if self.score > int(data["score"]):
            data["score"] = self.score
        with open("score.json", "w") as f:
            json.dump(data, f)

        while not self.alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.game.running = False
            self.game.screen.fill("black")
            font = pygame.font.Font("assets/megamax.ttf", 50)
            font2 = pygame.font.Font("assets/megamax.ttf", 20)
            score_text = font2.render(f"Score: {self.score}", True, (255, 0, 0))
            hscore_text = font2.render(f"High Score: {data["score"]}", True, (255, 0, 0))
            text = font.render("GAME OVER", True, (255, 0, 0))
            text_rect = text.get_rect()
            score_rect = score_text.get_rect()
            score_rect.center = (250, 300)
            hscore_rect = hscore_text.get_rect()
            hscore_rect.center = (250, 200)
            text_rect.center = (250, 250)
            self.game.screen.blit(hscore_text, hscore_rect)
            self.game.screen.blit(text, text_rect)
            self.game.screen.blit(score_text, score_rect)
            pygame.display.flip()
            pygame.display.update()