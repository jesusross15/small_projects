import sys
import pygame

# Imports the settings class created in settings.py
from settings import Settings
# Imports the ship class created in ship.py
from ship import Ship
# Imports the bullet class created in bullet.py
from bullet import Bullet

# This class will serve as the superclass to manage game assets and behavior
class AlienInvasion:
    def __init__(self):
        # This method serves as a way to initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, 
             self.settings.screen_height))
        pygame.display.set_caption("Alien Inavsion")
        
        # From ship class
        self.ship = Ship(self)
        
        # Bullet class
        self.bullets = pygame.sprite.Group()
        
        # Setting the background color
        # This color would be a light gray color (we can play around and change it later if we'd like)
        self.big_color = (230, 230, 230)
        
    def run_game(self):
        # Starts the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
    def _check_events(self):
        # Responds to keyboard and mouse movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        # Responds to keypresses
        if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE: # fires bullet when you hit space bar
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
 
                
    # Method for fireing bullet
    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
                          
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen        
        # Redraw the screen during each pass I make through the loop
        self.screen.fill(self.settings.bg_color)
        # From ship class
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # Makes the most recently drawn screen visible       
        pygame.display.flip()
        

if __name__ == "__main__":
    # Makes an instance of the game and runs the game 
    ai = AlienInvasion()
    ai.run_game()