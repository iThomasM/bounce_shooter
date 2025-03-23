class Config:
    def __init__(self):
        #Game
        self.screen_width = 500
        self.screen_height = 500
        self.money = 7
        self.score = 0
        #Player
        self.player_speed = 1
        self.sprint_speed = 1
        self.player_dashes = 5
        self.player_knockback_duration = 5
        self.player_knockback_amount = 30
        self.player_health = 100
        self.max_health = 100
        self.player_dashing_duration = 5
        #Enemies
        self.enemy_speed = 0.9
        self.max_enemies = 1
        self.spawn_cooldown = 90
        #Bullet
        self.bullet_cooldown = 120
        self.bullet_speed = 10
        #Pricing
        self.dash_price = 3
        self.speed_price = 7
        self.bullet_price = 6
        self.heal_price = 6