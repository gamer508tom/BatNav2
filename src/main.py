import pygame
import marine
import math
from player import Player

from croiseur import Croiseur
from porteavion import PorteAvion
from submersible import Submersible
from explorateur import Explorateur


LEFT = 1
RIGHT = 3
w, h = (1600, 900)
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = 1

name = 'player1'
color = 'blue'
position = [30, 30]
flotte = [{'type':Croiseur, 'position':[0, 50]},
			{'type':Croiseur, 'position':[0, 100]},
			{'type':Croiseur, 'position':[0, 150]},
			{'type':Croiseur, 'position':[0, 200]}]
player1 = Player(name, color, position, flotte, w, h)

#spriteGroup = pygame.sprite.Group()
#spriteGroup.add(marine.Marine(w, h, [10, 10]))

selected = None

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0			
			
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
			print "You pressed the left mouse button at (%d, %d)" % event.pos
			pos = pygame.mouse.get_pos()
			clicked_sprites = [s for s in player1 if s.rect.collidepoint(pos)]
			for i in clicked_sprites:
				selected = i
				print "selected object:", i
            
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
			print "You pressed the right mouse button at (%d, %d)" % event.pos
			if selected is None:
				print "First select an object"
				pass
			else:
				obj = selected
				pos = obj.rect
				dx = event.pos[0] - pos[0]
				dy = event.pos[1] - pos[1]
				obj.change_direction(dx, dy)
				print "new object direction:", obj.direction
	player1.update()
	screen.fill((255, 255, 255))             #wipes the screen
	player1.draw(screen)           #draws every Sprite object in this Group
	pygame.display.flip()
	clock.tick(40)
