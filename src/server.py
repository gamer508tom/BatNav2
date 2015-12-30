import pygame
import marine
import math
from player import Player
from Net import *

import os,sys

from croiseur import Croiseur
from porteavion import PorteAvion
from submersible import Submersible
from explorateur import Explorateur
from pirate import Pirate

from missile import Missile


HOST = "192.168.1.24"
PORT = 55555


pygame.mixer.init()
boom = pygame.mixer.Sound ("../sound/boom.wav")

clock = pygame.time.Clock()

LEFT = 1
MIDDLE = 2
RIGHT = 3
w, h = (1600, 900)

screen = pygame.display.set_mode((w, h))

name = 'player1'
color = 'blue'
position = [100, 300]
flotte = [{'type':Croiseur, 'position':[0, 50]},
			{'type':Submersible, 'position':[0, 100]},
			{'type':Explorateur, 'position':[0, 150]},
            {'type':Pirate, 'position':[0, 300]},
			{'type':PorteAvion, 'position':[0, 200]}]
player1 = Player(name, color, position, flotte, w, h)


name = 'player2'
color = 'red'
position = [1400, 300]
flotte = [{'type':Croiseur, 'position':[0, 50]},
			{'type':Submersible, 'position':[0, 100]},
			{'type':Explorateur, 'position':[0, 150]},
            {'type':Pirate, 'position':[0, 300]},
			{'type':PorteAvion, 'position':[0, 200]}]
player2 = Player(name, color, position, flotte, w, h)


missiles = pygame.sprite.Group()

map_objects = pygame.sprite.Group()
map_objects.add(missiles)
map_objects.add(player1)
map_objects.add(player2)


players = dict(player1=player1, 
				player2 = player2)


def adapt_to_socket(group):
	for i in group:
		#print i
		i.image = None
	return [(i.__class__.__name__, i.rect, i.direction) for i in group]

change = dict(player1=False, 
				player2 = False)
# INIT SERVER
sys.path.append(os.path.split(sys.path[0])[0])
class ServerHandler(TCPServer):
	def __init__(self):
		TCPServer.__init__(self)
	def connect_func(self,sock,host,port):
		print "Server successfully connected to %s on port %s!" % (host,port)

	def client_connect_func(self,sock,host,port,address):
		print "A client, (ip: %s, code: %s) connected on port %s!" % (address[0],address[1],port)

	def client_disconnect_func(self,sock,host,port,address):
		print "A client, (ip: %s, code: %s) disconnected from port %s!" % (address[0],address[1],port)
		raise
	def handle_data(self,data):
		global missiles, map_objects, players, player1, player2, change
		if len(data) > 1:
			if data[1] == LEFT:
				players[data[0]].left_click(data[2])
			elif data[1] == MIDDLE:
				players[data[0]].middle_click(data[2], missiles)
			elif data[1] == RIGHT:
				players[data[0]].right_click(data[2])
			map_objects = pygame.sprite.Group()
			map_objects.add(missiles)
			map_objects.add(player1)
			map_objects.add(player2)
			#print
			#print "send those objects:"
			#for s in map_objects:
				#print "sprite player", s, s.rect, s.direction
			#print "send_data because received", data
			self.send_data(adapt_to_socket(map_objects))
		elif len(data) > 0 and data[0] == "add self":
			self.send_data(adapt_to_socket(map_objects))
			print "send_data because received", data
		else:
			if len(data) > 0 and change[data[0]]:
				change[data[0]] = False
				map_objects = pygame.sprite.Group()
				map_objects.add(missiles)
				map_objects.add(player1)
				map_objects.add(player2)
				self.send_data(adapt_to_socket(map_objects))
		#print "send map", adapt_to_socket(map_objects)

from threading import Thread


def update_map():
	global map_objects, missiles, player1, player2, players, change
	while True:
		# Updates
		#print "update map objects"
		map_objects.update()
		# Process collisions
		d = pygame.sprite.groupcollide(missiles, missiles, False, False)
		for m in d.keys():
			for m2 in d[m]:
				if (not m == m2):
					m.kill()
					change["player1"] = True
					change["player2"] = True
					break
					
		# PLAYER1
		d = pygame.sprite.groupcollide(player1, missiles, False, False)
		for nav in d.keys():
			for m in d[nav]:
				nav_killed, explosion = nav.receive_missile(m)
				if nav_killed:
					nav.kill()
				change["player1"] = change["player1"] or explosion
				change["player2"] = change["player2"] or explosion
		if player1.selection is not None and not player1.selection.alive():
			player1.selection = None
			
		# PLAYER 2
		d = pygame.sprite.groupcollide(player2, missiles, False, False)
		for nav in d.keys():
			for m in d[nav]:
				nav_killed, explosion = nav.receive_missile(m)
				if nav_killed:
					nav.kill()
					boom.play()
				change["player1"] = change["player1"] or explosion
				change["player2"] = change["player2"] or explosion
		if player2.selection is not None and not player2.selection.alive():
			player2.selection = None
			
		clock.tick(10)

upd_process = Thread(target=update_map)
upd_process.start()	

def main():
    while True:
        try:
            server = ServerHandler()
            server.connect(HOST,PORT)
            server.serve_forever()
        except:
            try:
                server.quit()
            except:
                pass
    server.quit()


main()
	
