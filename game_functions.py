import sys

import pygame

def check_events(ship):
    """Resopnd to keypass and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""


