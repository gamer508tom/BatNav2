
import pygame
from marine import Marine

class Croiseur(Marine):
    def __init__(self, w, h, position):
        Marine.__init__(self, w, h, position)
        self.vision = 6
        self.vitesse = 1
        self.discretion = 0
        self.puissance = 4
