
import pygame
from marine import Marine

class Croiseur(Marine):
    def __init__(self, w, h, position):
        self.image = pygame.image.load('../img/croiseur.png').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 6
        self.vitesse = 0.5
        self.discretion = 0
        self.puissance = 4
