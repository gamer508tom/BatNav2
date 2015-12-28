 
import pygame
import time
from marine import Marine

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

