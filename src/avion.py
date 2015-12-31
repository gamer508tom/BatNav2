
import pygame
import time
from marine import Marine
from missile import Missile
from submersible import Submersible

class Avion(Marine):
    def __init__(self, w, h, position, direction=None, color=None):
        self.image = pygame.image.load('../img/avion.png').convert()
        Marine.__init__(self, w, h, position)
        self.name = 'avion'
        self.vision = 20
        self.vitesse = 4.
        self.discretion = 0
        self.puissance = 3
        self.recharge = 2
        self.time_recharge = 5
        self.vie = 5
        self.last_recharge = time.time()
        self.munition = self.recharge
        self.flying = True
        self.direction = direction
        self.update_color(color)

    def do_recharge(self):
        if self.puissance > 0 and self.munition < self.recharge and time.time() - self.last_recharge > self.time_recharge:
            if not self.flying:
                self.last_recharge = time.time()
                self.munition = self.munition + 1
            
    def touch_by_missile(self, m):
        if m.tireur == self or isinstance(m.tireur, Submersible):
            return False
        else:
            return True
            
    def create_missile(self, direction):        
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self)

