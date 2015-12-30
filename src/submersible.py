 
import pygame
import time
from marine import Marine
from missile import Missile

class Submersible(Marine):
    def __init__(self, w, h, position, direction=None):
        self.image = pygame.image.load('../img/submersible.png').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 6
        self.vitesse = 0.3
        self.discretion = 0
        self.puissance = 3
        self.recharge = 10
        self.time_recharge = 5
        self.last_recharge = time.time()
        self.munition = 10
        self.direction = direction
                
    def touch_by_missile(self, m):
        if m.tireur == self or m.tireur.__class__.__name__ == "Croiseur" or m.tireur.__class__.__name__ == "PorteAvion":
            return False
        else:
            return True
            
    def create_missile(self, direction):        
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self)


