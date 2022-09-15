# This class will serve ad the class that stores all the settings for the game
class Settings:
    
    #Initializing the game's settings
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        #Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        # rgb for pure red
        self.bullets_allowed = 50
        
        # Ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3
        
        # How quickly the game speeds up
        self.speedup_scale = 1.4
        self.initialize_dynamic_settings()

# This method initializes the initial values for the ship, bullet and alien speeds
    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        # Increase speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale