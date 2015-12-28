
import pygame
from marine import Marine

class PorteAvion(Marine):
    def __init__(self, w, h, position):
        self.image = pygame.image.load('../img/porteavion.jpg').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 5
        self.vitesse = 0.2
        self.discretion = 0
        self.puissance = 2
        self.recharge = 10
