import pygame
from pygame.sprite import Sprite

ALIEN_IMAGE = {'alien_one' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_200x200.bmp",
'alien_two' : "H:\SpaceApes\SpaceApes-Programing\Projects\python_game\images\\alien_invasion_alien1_200x100.bmp"}

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialises the alien and sets its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image 1 and set its rect attribute.
        self.image = pygame.image.load(ALIEN_IMAGE['alien_two'])
        self.rect = self.image.get_rect()

        # Start each new alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact position.
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the alien at the current location."""
        self.screen.blit(self.image, self.rect)