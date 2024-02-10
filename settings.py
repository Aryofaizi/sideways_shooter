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
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        
        # dynamic settings
        self.initialize_dynamic_settings()
        
        # jet
        self.jet_limit = 3
        
        # speed_up game
        self.speedup_scale = 1.1
        
    def initialize_dynamic_settings(self):
        """dynamic setting get initialized with this method"""
        self.bullet_speed = 1.5
        # enemy position
        self.enemy_freqeuncy = 0.001
        self.enemy_speed = 0.5
        