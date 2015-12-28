
import pygame
from marine import Marine

class Explorateur(Marine):
    def __init__(self, w, h, position):
        Marine.__init__(self, w, h, position)
        self.vision = 10
        self.vitesse = 1.25
        self.discretion = 0
        self.puissance = 0
