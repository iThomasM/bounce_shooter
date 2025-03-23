class Config:
    def __init__(self):
        #Game
        self.screen_width = 500
        self.screen_height = 500
        #Player
        self.player_speed = 1
        self.sprint_speed = 1
        self.player_knockback_duration = 5
        self.player_knockback_amount = 30
        #Enemies
        self.enemy_speed = 1.5
        self.max_enemies = 1
        self.spawn_cooldown = 60
        self.player_dashing_duration = 5
        #Bullet
        self.bullet_cooldown = 600
        self.bullet_speed = 10