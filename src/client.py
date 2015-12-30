import pygame
from pygame.locals import *
import os,sys
sys.path.append(os.path.split(sys.path[0])[0])
from Net import *

cont = True
while cont:
    name = raw_input("What is your name?  ")
    for char in name:
        if char != " ":
            cont = False
            break

client = TCPClient()
PORT = 6552
client.connect("localhost",PORT)
client.send_data(["add self"])

bg = pygame.image.load("../img/font.png")
screen.blit(bg,(0,0))

clock = pygame.time.Clock()
w, h = (1600, 900)
LEFT = 1
MIDDLE = 2
RIGHT = 3

screen = pygame.display.set_mode((w, h))


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
                for cls, rect, direction in vue:
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
    global vue
    while True:
        GetInput()
        Update()
        #Draw()
main()
