
import time
import pygame
from marine import Marine
from missile import Missile

class Croiseur(Marine):
    def __init__(self, w, h, position, direction=None, color=None):
        self.image = pygame.image.load('../img/croiseur.png').convert()
        Marine.__init__(self, w, h, position)
        self.name = 'croiseur'
        self.vision = 6
        self.vitesse = 1.
        self.discretion = 0
        self.puissance = 4
        self.recharge = 10
        self.time_recharge = 5
        self.vie = 11
        self.last_recharge = time.time()
        self.munition = 10
        self.direction = direction
        self.update_color(color)
        
    def touch_by_missile(self, m):
        if m.tireur == self:
            return False
        else:
            return True

    def create_missile(self, direction):        
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self)

