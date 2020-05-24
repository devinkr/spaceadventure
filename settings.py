class Settings:
    """A class to represent all in game settings"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.fullscreen = False
        self.screen_width = 1024
        self.screen_height = 640
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3
        self.ship_size = (50, 34)

        # Bullet settings
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (200, 200, 200)

        self.initialize_dynamic_settings()

        # Level scale
        self.speed_scale = 1 + (self.level / 5)
        self.score_scale = 1 + (self.level / 5)

    
    def initialize_dynamic_settings(self):
        self.game_active = False
        self.ship_speed = 1.0
        self.bullet_speed = 3.0

        # Asteroid settings
        self.asteroid_speed = 1
        self.max_asteroids = 5

        # Scoring
        self.asteroid_points = 50
        self.level = 1

    def increase_speed(self):
        """Increase speed of asteroids and points value"""
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.asteroid_speed *= self.speed_scale
        self.asteroid_points = int(self.asteroid_points * self.score_scale)