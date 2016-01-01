 
import pygame
import math
from marine import Marine
pygame.mixer.init()
avionshot = pygame.mixer.Sound("../sound/avionshot.wav")
pygame.mixer.init()
submersibleshot = pygame.mixer.Sound("../sound/submersibleshot.wav")
pygame.mixer.init()
bateaushot = pygame.mixer.Sound("../sound/bateaushot.wav")

class Missile(Marine):
    def __init__(self, w, h, position, direction, color=None, puissance=2, tireur=None):
        print color, tireur.__class__.__name__ 
        if tireur.__class__.__name__ == "Avion":
            self.image = pygame.image.load("../img/missileavion.png").convert()
            avionshot.play()    
            self.color = "air"
        elif tireur.__class__.__name__ == "Croiseur":
            self.image = pygame.image.load("../img/missilebateau.png").convert() 
            bateaushot.play()  
            self.color = "sol"
        elif tireur.__class__.__name__ == "PorteAvion":
            self.image = pygame.image.load("../img/missilebateau.png").convert()
            bateaushot.play() 
            self.color = "sol"
        elif tireur.__class__.__name__ == "Submersible":
            self.image = pygame.image.load("../img/missilesubmersible.png").convert()
            submersibleshot.play() 
            self.color = "eau"
        else:     
            self.color = color
            if color == "air":
                self.image = pygame.image.load("../img/missileavion.png").convert()
            elif color == "sol":
                self.image = pygame.image.load("../img/missilebateau.png").convert() 
            elif color == "eau":
                self.image = pygame.image.load("../img/missilesubmersible.png").convert()
                
        Marine.__init__(self, w, h, position, self.color)
        self.vitesse = 5.
        self.discretion = 0
        self.puissance = puissance
        self.change_direction(direction[0], direction[1])
        self.tireur = tireur   

    def update(self):
        if self.direction is not None:
            move = [0., 0.]
            move[0] = self.vitesse * self.direction[0] + self.offset[0]
            self.offset[0] = math.modf(move[0])[0] # decimal part
            move[1] = self.vitesse * self.direction[1] + self.offset[1]
            self.offset[1] = math.modf(move[1])[0]
            if move[0] + self.rect[0] + self.rect[2] > self.w or move[0] + self.rect[0] < 0:
                self.kill()
            if move[1] + self.rect[1] + self.rect[3] > self.h or move[1] + self.rect[1] < 0:
                self.kill()
            self.rect = self.rect.move(move)
            #print move        
        pygame.event.pump()
