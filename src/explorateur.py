
import pygame
from marine import Marine

class Explorateur(Marine):
    def __init__(self, w, h, position, direction=None):
        self.image = pygame.image.load('../img/explorateur.png').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 10
        self.vitesse = 1.5
        self.discretion = 0
        self.puissance = 0
        self.direction = direction
        
    def touch_by_missile(self, m):
        if m.tireur == self:
            return False
        else:
            return True
