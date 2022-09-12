import sys
from turtle import Screen
import pygame

# Imports the settings class
from settings import Settings
# Imports the ship class
from ship import Ship

# This class will serve as the superclass to manage game assets and behavior
class AlienInvasion:
    def __init__(self):
        # This method serves as a way to initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Inavsion")
        
        # From ship class
        self.ship = Ship(self)
        # Setting the background color
        # This color would be a light gray color (we can play around and change it later if we'd like)
        self.big_color = (230, 230, 230)
        
    def run_game(self):
        # Starts the main loop for the game
        while True:
            # Watches keyboard and mouse "events" (movements)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Fill the screen with the color chose and redraw the screen during each pass I make through the loop
            self.screen.fill(self.settings.bg_color)
            # From ship class
            self.ship.blitme()
            
            # Makes the most recently drawn screen visible       
            pygame.display.flip()
            

if __name__ == "__main__":
    # Makes an instance of the game and runs the game 
    ai = AlienInvasion()
    ai.run_game()