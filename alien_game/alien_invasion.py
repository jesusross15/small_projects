import sys
import pygame

# Imports the settings class created in settings.py
from settings import Settings
# Imports the ship class created in ship.py
from ship import Ship
# Imports the bullet class created in bullet.py
from bullet import Bullet
# Imports alien class created in alien.py
from alien import Alien

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
        
        # Alien class
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        # Setting the background color
        # This color would be a light gray color (we can play around and change it later if we'd like)
        self.big_color = (230, 230, 230)
        
    def run_game(self):
        # Starts the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    
    def _update_bullets(self):       
        # Update the bullet's position
        self.bullets.update()
        # Get rid of the bullets that have disappeared bc they take up too much memory
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets)) this is to check if the bullets actually disappear from the screen            
    
    def _update_aliens(self):
        # Check if the fleet is at an edge then update the positions of all aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()
                   
    def _create_fleet(self):
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
    
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
        
    def _create_alien(self, alien_number, row_number):    
        # Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        
        
    def _check_fleet_edges(self):
        # Respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        # Drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
                          
    def _update_screen(self):
        # Update images on the screen, and flip to the new screen        
        # Redraw the screen during each pass I make through the loop
        self.screen.fill(self.settings.bg_color)
        # From ship class
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
            
        # Makes the most recently drawn screen visible       
        pygame.display.flip()
        

if __name__ == "__main__":
    # Makes an instance of the game and runs the game 
    ai = AlienInvasion()
    ai.run_game()