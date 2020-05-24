import sys
from time import sleep

import pygame

from settings import Settings
from sprites import Ship, Asteroid

class SpaceAdventure:
    """ A Space adventure game"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption("Devin's Space Adventure")

        self.ship = Ship(self)
        self.asteroids = pygame.sprite.Group()

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._listento_events()
            self.ship.update()
            self._update_asteroids()
            self._update_screen()

    def _update_screen(self):
        """Update everything on screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.asteroids.draw(self.screen)
        pygame.display.flip()

    def _listento_events(self):
        """Listen for clicks and keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown(event)
            elif event.type == pygame.KEYUP:
                self._keyup(event)

    def _keydown(self, event):
        """"Respond to keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            # quit
            sys.exit()
        elif event.key == pygame.K_r:
            #New game
            print("New Game")
        elif event.key == pygame.K_SPACE:
            print("Bang Bang")

    def _keyup(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _create_asteroid(self):
        if len(self.asteroids) < self.settings.max_asteroids:
            asteroid = Asteroid(self)
            self.asteroids.add(asteroid)

    def _update_asteroids(self):
        self._create_asteroid()
        self.asteroids.update()
        for asteroid in self.asteroids.copy():
            if asteroid.rect.right < 0:
                self.asteroids.remove(asteroid)



if __name__ == "__main__":
    sa = SpaceAdventure()
    sa.run_game()