import pygame



class Player(pygame.sprite.Group):
    def __init__(self, name, color, position, flotte, w, h):
        self.name = name
        pygame.sprite.Group.__init__(self)
        for m in flotte:
            self.add(m['type'](w, h, [position[0] + m['position'][0], position[1] + m['position'][1]]))
