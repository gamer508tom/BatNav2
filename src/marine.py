import pygame
import math

class Marine(pygame.sprite.Sprite):
    def __init__(self, w, h, position):
        pygame.sprite.Sprite.__init__(self)
        self.w = w
        self.h = h
        self.rect = self.image.get_rect()
        self.state = "still"
        self.direction = None
        self.vie = 10
        self.vitesse = 1.
        self.rect = self.rect.move(position)
        self.offset = [0., 0.]

    def update(self):
        if self.direction is not None:
            move = [0., 0.]
            move[0] = self.vitesse * self.direction[0] + self.offset[0]
            self.offset[0] = math.modf(move[0])[0] # decimal part
            move[1] = self.vitesse * self.direction[1] + self.offset[1]
            self.offset[1] = math.modf(move[1])[0]
            if move[0] + self.rect[0] + self.rect[2] > self.w or move[0] + self.rect[0] < 0:
                move[0] = 0
            if move[1] + self.rect[1] + self.rect[3] > self.h or move[1] + self.rect[1] < 0:
                move[1] = 0
            self.rect = self.rect.move(move)
            #print move        
        pygame.event.pump()

    def change_direction(self, dx, dy):
        norm = math.sqrt(dx*dx + dy*dy)
        self.direction = [dx/norm, dy/norm]
        self.state = "moving"
