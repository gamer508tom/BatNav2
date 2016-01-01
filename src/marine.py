import pygame
import math
import time
class Marine(pygame.sprite.Sprite):
    def __init__(self, w, h, position, color=None):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.w = w
        self.h = h
        self.rect = self.image.get_rect()
        self.state = "still"
        self.direction = None
        self.vie = 10
        self.vitesse = 2.
        self.rect = self.rect.move(position)
        self.offset = [0., 0.]

    def update(self):
        #print "marine update", self
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
            #print "marine new rect", self.rect
        self.do_recharge()
        pygame.event.pump()
        
    def do_recharge(self):
        if self.puissance > 0 and self.munition < self.recharge and time.time() - self.last_recharge > self.time_recharge:
            self.last_recharge = time.time()
            self.munition = self.munition + 1        
        
    def double_click(self):
        pass

    def change_direction(self, dx, dy):
        norm = math.sqrt(dx*dx + dy*dy)
        self.direction = [dx/norm, dy/norm]
        self.state = "moving"
        
    def touch_by_missile(self, m):
        pass
        
    def receive_missile(self, m):
        if self.touch_by_missile(m):
            self.vie = self.vie - m.puissance
            m.kill()
            if self.vie < 1:
                self.kill()
                return True, True
            else:
                return False, True
        else:
            return False, False
            
    def fire(self):
        if self.munition > 0:
            self.munition = self.munition - 1
            return True
        else:
            return False
            
    def update_color(self, color):
        if color is not None:
            self.image = pygame.image.load('../img/' + self.name + color + '.png').convert()
            self.color = color
