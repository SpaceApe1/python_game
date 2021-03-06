import pygame
from pygame.sprite import Sprite

# windows path
"""ALIEN_IMAGE = {
    'alien_one' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_200x200.bmp",
    'alien_two' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_200x100.bmp",
    'alien_three' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_100x50.bmp"}
"""

# mac path
ALIEN_IMAGE = {
    'alien_one' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_200x200.bmp",
    'alien_two' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_200x100.bmp",
    'alien_three' : "/Users/kaihubner/Documents/GitHub/python_game/images/alien_invasion_alien1_100x50.bmp"}

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialises the alien and sets its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image 1 and set its rect attribute.
        self.image = pygame.image.load(ALIEN_IMAGE['alien_three'])
        self.rect = self.image.get_rect()

        # Start each new alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at the current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True