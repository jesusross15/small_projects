class GameStats:
    # Track the in game stats
    def __init__(self, ai_game):
        # Initialize the stats
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = False
        
    def reset_stats(self):
        # Initialize the statistics that can run during the game
        self.ships_left = self.settings.ship_limit