
import pygame
from marine import Marine

class PorteAvion(Marine):
    def __init__(self, w, h, position):
        Marine.__init__(self, w, h, position)
        self.vision = 5
        self.vitesse = 0.5
        self.discretion = 0
        self.puissance = 2
        self.recharge = 10
