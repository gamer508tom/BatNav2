
import pygame
import time
from marine import Marine
from avion import Avion
from missile import Missile

class PorteAvion(Marine):
    def __init__(self, w, h, position, direction=None, color=None):
        self.image = pygame.image.load('../img/porteavion.png').convert()
        Marine.__init__(self, w, h, position)
        self.name = 'porteavion'
        self.vision = 5
        self.vitesse = 0.4
        self.discretion = 0
        self.puissance = 2
        self.recharge = 10
        self.time_recharge = 5
        self.last_recharge = time.time()
        self.munition = 10
        self.direction = direction
        self.update_color(color)
        
        self.n_avions = 1
        self.avion = None
        
    def update(self):
        Marine.update(self)
        if self.avion is not None:
            if self.avion.rect.colliderect(self.rect):
                self.avion.kill()
                self.avion = None
                self.n_avions = self.n_avions + 1
                
    def launch(self):
        if self.n_avions > 0:
            self.n_avions = self.n_avions - 1
            print self.color
            if self.color == "bleu":
                avion = Avion(self.w, self.h, [self.rect.centerx + 80, self.rect.centery - 5], [1., 0.], self.color)
            elif self.color == "rouge":
                avion = Avion(self.w, self.h, [self.rect.centerx - 80, self.rect.centery] - 5, [-1., 0.], self.color)
            for g in self.groups():
                g.add(avion)
                self.avion = avion
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
        return Missile(self.w, self.h, [self.rect.centerx, self.rect.centery], direction, self.puissance, self)
