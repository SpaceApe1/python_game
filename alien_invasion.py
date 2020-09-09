import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Initial pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make a Alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)    
run_game()