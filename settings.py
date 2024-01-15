class Settings:
    """class to set game settings like screen width or ..."""
    
    def __init__(self):
        """initialize game settings."""
        self.screen_width = 700
        self.screen_height = 1_000
        self.bg_color = (255, 255, 255)
        self.jet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_speed = 1.5
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        # enemy position
        self.enemy_freqeuncy = 0.001
        self.enemy_speed = 0.5