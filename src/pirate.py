
import pygame
from marine import Marine

class Pirate(Marine):
    def __init__(self, w, h, position):
        self.image = pygame.image.load('../img/pirate.png').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 5
        self.vitesse = 0.3
        self.discretion = 0
        self.puissance = 0
        self.vie = 1
        
    def touch_by_missile(self, m):
        if m.tireur == self:
            return False
        else:
            return True