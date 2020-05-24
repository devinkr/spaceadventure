""" File holding all the sprite classes """
from random import randrange

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Player spaceship"""
    def __init__(self, sa_game):
        super().__init__()
        self.settings = sa_game.settings
        self.screen = sa_game.screen
        self.screen_rect = sa_game.screen.get_rect()

        # Load ship image and get its size
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.image = pygame.transform.scale(self.image, self.settings.ship_size)
        self.rect = self.image.get_rect()

        # Start ship at center of left side of screen
        self.rect.midleft = self.screen_rect.midleft

        # Store decimal value for ships x, y position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position basd on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Asteroid(Sprite):
    """ Asteroids that move across screen"""
    def __init__(self, sa_game):
        super().__init__()
        self.settings = sa_game.settings
        self.screen = sa_game.screen
        self.screen_rect = sa_game.screen.get_rect()

        # Load asteroid image and make random size
        asteroid_scale = (randrange(30, 100) / 100)
        self.image = pygame.image.load('images/asteroid.bmp').convert()
        self.size = self.image.get_size()
        scale_w = int(self.size[0] * asteroid_scale)
        scale_h = int(self.size[1] * asteroid_scale)
        self.image = pygame.transform.scale(self.image, (scale_w, scale_h))
        self.rect = self.image.get_rect()

        # Start asteroid just off right side of screen
        self.rect.left = self.screen_rect.right + 10
        y_rand = randrange(self.screen_rect.top, self.screen_rect.bottom)
        self.rect.top = y_rand

        # Store decimal value for asteroids x, y position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Individual random asteroid speed
        asteroid_speed = (randrange(30, 100) / 100)
        self.asteroid_speed = (self.settings.asteroid_speed * asteroid_speed)
    
    def update(self):
        """Move asteroids to the left at random speed"""
        self.x -= (self.asteroid_speed)
        self.rect.x = self.x

class Bullets(Sprite):
    """ bullets fired from ship"""
    def __init__(self, sa_game):
        super().__init__()

