import pygame
from pygame.locals import *
import os,sys
sys.path.append(os.path.split(sys.path[0])[0])
from Net import *

from croiseur import Croiseur
from porteavion import PorteAvion
from submersible import Submersible
from explorateur import Explorateur
from pirate import Pirate
from missile import Missile
from avion import Avion

cont = True
while cont:
    name = raw_input("What is your name?  ")
    for char in name:
        if char != " ":
            cont = False
            break

client = TCPClient()
HOST = "192.168.1.24"
PORT = 55555

client.connect(HOST,PORT)
client.send_data(["add self"])


clock = pygame.time.Clock()
w, h = (1600, 900)
LEFT = 1
MIDDLE = 2
RIGHT = 3

screen = pygame.display.set_mode((w, h))

bg = pygame.image.load("../img/font.png")
screen.blit(bg,(0,0))

vue = None
sendingdata = [name]

                
def Update():
    global vue, vue_changed, sendingdata
    #print "update"
    data = client.check_for_data()
    if data is not None and len(data) > 0:        
        #print "data received", data
        vue = data
        vue_changed = True
    client.send_data(sendingdata)
    sendingdata = [name]


def GetInput():
    global name, sendingdata
    #print "get input"
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0			
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print "You pressed the left mouse button at (%d, %d)" % event.pos
            sendingdata = [name, LEFT, event.pos]
                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == MIDDLE:
            print "You pressed the middle mouse button at (%d, %d)" % event.pos
            sendingdata = [name, MIDDLE, event.pos]
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print "You pressed the right mouse button at (%d, %d)" % event.pos
            sendingdata = [name, RIGHT, event.pos]
                

vue_changed = True
draw_group = None

def Draw():
    global vue, draw_group, vue_changed
    while True:
        screen.blit(bg,(0,0))
        #print "draw loop", vue, vue_changed, draw_group
        if vue is not None:
            if vue_changed:
                vue_changed = False
                print "-----------re build vue", vue_changed
                draw_group = pygame.sprite.Group()
                for cls_name, rect, direction in vue:
                    if cls_name == "Avion":
                        cls = Avion
                    elif cls_name == "Croiseur":
                        cls = Croiseur
                    elif cls_name == "Explorateur":
                        cls = Explorateur
                    elif cls_name == "PorteAvion":
                        cls = PorteAvion
                    elif cls_name == "Submersible":
                        cls = Submersible
                    elif cls_name == "Missile":
                        cls = Missile
                    elif cls_name == "Pirate":
                        cls = Pirate
                    draw_group.add(cls(w, h, [rect[0], rect[1]], direction))
            draw_group.update()
            draw_group.draw(screen)
            #print "draw"
        pygame.display.flip()
        clock.tick(20)

from threading import Thread

upd_process = Thread(target=Draw)
upd_process.start()

def main():
    global vue, client
    while True:
        try:
            while True:
                GetInput()
                Update()
                #Draw()
        except:      
            try:      
                client.quit()
                client = TCPClient()
                client.connect(HOST,PORT)
                client.send_data(["add self"])
            except:
                pass
main()
