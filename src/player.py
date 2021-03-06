import pygame
from missile import Missile


class Player(pygame.sprite.Group):
    def __init__(self, name, color, position, flotte, w, h):
        self.name = name
        pygame.sprite.Group.__init__(self)
        for m in flotte:
            self.add(m['type'](w, h, [position[0] + m['position'][0], position[1] + m['position'][1]]))
        self.selection = None
        self.w = w
        self.h = h

    def left_click(self, pos):
        print "player", self.name, "left", pos
        clicked_sprites = [s for s in self if s.rect.collidepoint(pos)]
        print "clicked sprites", clicked_sprites
        for i in clicked_sprites:
            if i == self.selection:
                i.double_click()
            else:
                self.selection = i
            print "selected object:", i
        
    def middle_click(self, pos, missiles):
        print "player", self.name, "middle", pos
        if self.selection is None:
            print "First select an object"
            pass
        else:
            boat = self.selection
            puissance = boat.puissance
            if puissance > 0:
                if boat.fire():						
                    boat_pos = boat.rect					
                    dx = pos[0] - boat_pos.centerx
                    dy = pos[1] - boat_pos.centery
                    direction = [dx, dy]
                    missile = boat.create_missile(direction)
                    print "player missile", missile.color
                    missiles.add(missile)
        
    def right_click(self, pos):
        print "player", self.name, "right", pos
        if self.selection is None:
            pass
            print "first select an object"
        else:
            obj = self.selection
            if obj.rect.collidepoint(pos):
                obj.direction = None
                print "stop object"
            else:
                dx = pos[0] - obj.rect.centerx
                dy = pos[1] - obj.rect.centery
                obj.change_direction(dx, dy)
                print "new object direction:", obj.direction, obj, obj.groups()
