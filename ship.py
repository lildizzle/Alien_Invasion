import pygame

class Ship:
    def __init__(self,screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # load the shipand get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom= self.screen_rect.bottom
        self.moving_right = False
    def update(self):
        """Update the ship's positions based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
