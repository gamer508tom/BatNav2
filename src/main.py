import pygame
import marine
import math
from player import Player

from croiseur import Croiseur
from porteavion import PorteAvion
from submersible import Submersible
from explorateur import Explorateur

from missile import Missile


LEFT = 1
MIDDLE = 2
RIGHT = 3
w, h = (1600, 900)
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = 1

name = 'player1'
color = 'blue'
position = [30, 30]
flotte = [{'type':Croiseur, 'position':[0, 50]},
			{'type':Submersible, 'position':[0, 100]},
			{'type':Explorateur, 'position':[0, 150]},
			{'type':PorteAvion, 'position':[0, 200]}]
player1 = Player(name, color, position, flotte, w, h)

missiles = pygame.sprite.Group()

selected = None

while running:
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0			
			
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
			print "You pressed the left mouse button at (%d, %d)" % event.pos
			player1.left_click(event.pos)
				
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == MIDDLE:
			print "You pressed the middle mouse button at (%d, %d)" % event.pos
			player1.middle_click(event.pos, missiles)
            
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
			print "You pressed the right mouse button at (%d, %d)" % event.pos
			player1.right_click(event.pos)
			
	# Updates
	player1.update()
	missiles.update()
	
	# Process collisions
	d = pygame.sprite.groupcollide(missiles, missiles, False, False)
	for m in d.keys():
		for m2 in d[m]:
			if (not m == m2) and ((m.aerien and m2.aerien) or (not m.aerien and not m2.aerien)):
				m.kill()
				break
	d = pygame.sprite.groupcollide(player1, missiles, False, False)
	for nav in d.keys():
		for m in d[nav]:
			nav_killed = nav.receive_missile(m)
			if nav_killed:
				if player1.selection == nav:
					player1.selection = None
				nav.kill()
	
	# Draw
	screen.fill((255, 255, 255))
	player1.draw(screen)
	missiles.draw(screen)
	pygame.display.flip()
	clock.tick(40)
