import sys

import pygame

from settings import Settings

def run_game():
    # Initial pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_with, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ste the background color.
    bg_color = (230, 230, 230)

    # Start the main loop
    while True:

        # watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen  during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # Make the most recently draw screen visiblae.
        pygame.display.flip()
    
run_game()