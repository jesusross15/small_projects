import pygame

# This class will serve as a way to move/manage the object of a ship
class Ship:
    
    def __init__(self, ai_game):
        # Initialize the ship and set it's starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        # Draws the ship and its current location
        self.screen.blit(self.image, self.rect)