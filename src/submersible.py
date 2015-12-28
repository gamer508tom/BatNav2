 
import pygame
import time
from marine import Marine
from missile import Missile
from croiseur import Croiseur
import porteavion

class Submersible(Marine):
    def __init__(self, w, h, position):
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
                
    def touch_by_missile(self, m):
        if m.tireur == self or isinstance(m.tireur, Croiseur) or isinstance(m.tireur, porteavion.PorteAvion):
            return False
        else:
            return True
            
    def create_missile(self, direction):        
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self)


