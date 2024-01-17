class GameStats:
    """set game statistics."""
    
    def __init__(self, game):
        """initializing game statistics."""
        self.settings = game.settings
        self.game_reset()
        
    def game_reset(self):
        """resets game statistics."""
        self.jet_left = self.settings.jet_limit
        