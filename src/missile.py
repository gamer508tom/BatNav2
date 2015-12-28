 
import pygame
from marine import Marine

class Missile(Marine):
    def __init__(self, w, h, position, direction, puissance):
        self.image = pygame.image.load('../img/missile.jpg').convert()
        Marine.__init__(self, w, h, position)
        self.vitesse = 2.
        self.discretion = 0
        self.puissance = puissance
        self.change_direction(direction[0], direction[1])
