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
        self.bullet_speed = 4.0
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        # rgb for pure red
        self.bullets_allowed = 50
        
        # Ship settings
        self.ship_speed = 2.0