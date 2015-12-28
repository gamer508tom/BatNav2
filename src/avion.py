
import pygame
from marine import Marine

class Avion(Marine):
    def __init__(self, w, h, position):
        Marine.__init__(self, w, h, position)
        self.vision = 5
        self.vitesse = 1.5
        self.discretion = 0
        self.puissance = 3
        self.recharge = 10
