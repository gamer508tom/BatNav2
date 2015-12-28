
import pygame
import time
from marine import Marine

class Avion(Marine):
    def __init__(self, w, h, position):
        self.image = pygame.image.load('../img/avion.png').convert()
        Marine.__init__(self, w, h, position)
        self.vision = 20
        self.vitesse = 2
        self.discretion = 0
        self.puissance = 3
        self.recharge = 2
        self.time_recharge = 5
        self.last_recharge = time.time()
        self.munition = 10
        self.flying = False

    def do_recharge(self):
        if self.puissance > 0 and self.munition < self.recharge and time.time() - self.last_recharge > self.time_recharge:
            if not self.flying:
                self.last_recharge = time.time()
                self.munition = self.munition + 1
            
