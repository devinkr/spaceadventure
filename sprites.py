""" File holding all the sprite classes """
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Player spaceship"""
    super().__init__()


class Asteroid(Sprite):
    """ Asteroids that move across screen"""
    super().__init__()


class Bullets(Sprite):
    """ bullets fired from ship"""
    super().__init__()

