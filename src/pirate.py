
import pygame
from marine import Marine

class Pirate(Marine):
    def __init__(self, w, h, position, direction=None, color=None):
        self.image = pygame.image.load('../img/pirate.png').convert()
        Marine.__init__(self, w, h, position)
        self.name = 'pirate'
        self.vision = 5
        self.vitesse = 1.5
        self.discretion = 0
        self.puissance = 0
        self.vie = 1
        self.direction = direction
        self.update_color(color)
        
    def touch_by_missile(self, m):
        if m.tireur == self:
            return False
        else:
            return True
