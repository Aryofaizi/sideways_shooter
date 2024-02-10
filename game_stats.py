class GameStats:
    """set game statistics."""
    
    def __init__(self, game):
        """initializing game statistics."""
        self.settings = game.settings
        self.game_reset()
        
        # game active flag
        self.game_active = False
        self.high_score = 0
        
    def game_reset(self):
        """resets game statistics."""
        self.jet_left = self.settings.jet_limit
        
        # score 
        self.score = 0
        self.enemies_shot_down = 0
        self.game_level = 1