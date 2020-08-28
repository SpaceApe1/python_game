import pygame
import sys

from PIL import Image

SHIP_IMAGES = {'ship_one': 'alien_invasion_ship1.bmp'}

class Ship():

    def __init__(self,screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        """Quelle: https://www.geeksforgeeks.org/python-pil-image-resize-method/
        reszie all images to same szise
        """
        ship_image = ''
        while ship_image == '':
            new_ship_size = (50, 50)
            try:
                loaded_ship_image = Image.open(SHIP_IMAGES['ship_one'])
                ship_image = loaded_ship_image.resize(new_ship_size)
            except:
                print('Exception ', sys.exc_info()[0], ' occured.')    

        self.image = pygame.image.load(ship_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """"Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

"""
aktuell kommt das ship in einem falschen format
"""