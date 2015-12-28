 
import pygame
from marine import Marine

class Submersible(Marine):
    def __init__(self, w, h, position):
        Marine.__init__(self, w, h, position)
        self.vision = 6
        self.vitesse = 0.4
        self.discretion = 0
        self.puissance = 3
        self.recharge = 10
