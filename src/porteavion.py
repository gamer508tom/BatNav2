
import pygame
import time
from marine import Marine
from avion import Avion
from missile import Missile

class PorteAvion(Marine):
    def __init__(self, w, h, position):
        self.image = pygame.image.load('../img/porteavion.jpg').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 5
        self.vitesse = 0.2
        self.discretion = 0
        self.puissance = 2
        self.recharge = 10
        self.time_recharge = 5
        self.last_recharge = time.time()
        self.munition = 10
        
        self.n_avions = 1
        
    def launch(self):
        if self.n_avions > 0:
            self.n_avions = self.n_avions - 1
            avion = Avion(self.w, self.h, [self.rect[0], self.rect[1]])
            for g in self.groups():
                g.add(avion)
        else:
            return False
            
    def double_click(self):
        self.launch()
        
    def touch_by_missile(self, m):
        if m.tireur == self:
            return False
        else:
            return True

    def create_missile(self, direction):        
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self, True)
