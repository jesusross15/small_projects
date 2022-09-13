import pygame

# This class will serve as a way to move/manage the object of a ship
class Ship:
    
    def __init__(self, ai_game):
        # Initialize the ship and set it's starting position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rectangle
        self.image = pygame.image.load("alien_game/images/ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        # Update the ship's position based on the movement flags
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        
        
    def blitme(self):
        # Draws the ship and its current location
        self.screen.blit(self.image, self.rect)