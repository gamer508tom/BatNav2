
import time
import pygame
from marine import Marine
from missile import Missile

class Croiseur(Marine):
    def __init__(self, w, h, position):
        self.image = pygame.image.load('../img/croiseur.png').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 6
        self.vitesse = 0.5
        self.discretion = 0
        self.puissance = 4
        self.recharge = 10
        self.time_recharge = 5
        self.last_recharge = time.time()
        self.munition = 10

    def create_missile(self, direction):        
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self, True)
        
    def touch_by_missile(self, m):
        if m.tireur == self:
            return False
        else:
            return True
