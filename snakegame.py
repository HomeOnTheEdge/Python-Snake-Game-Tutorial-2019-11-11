# -*- coding: utf-8 -*-
"""
Snake Game Python Tutorial
https://www.youtube.com/watch?v=CD4qAhfFuLo
Oct 31, 2018
freeCodeCamp.org


'How to install pygame'
https://www.youtube.com/watch?v=E-WhAS6qzsU
How to Install Pygame on Mac OSX (Fast-Simple)
1) Open Terminal
2) In Terminal, enter: curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
3) In Terminal, enter: sudo pip install pygame
4) In Terminal, enter: IDLE
5) In IDLE, enter: import pygame
    If no errors, then pygame has been installed successfully!
"""

import math
import random
import pygame #See namespace on 'How to install pygame'
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass
    
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass
    
class snake(object):
    def __init__(self, color, pos):
        pass
    
    def move(self):
        pass
    
    def reset(self, pos):
        pass
    
    def addCube(self):
        pass
    
    def draw(self, surface):
        pass
    
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
    
    
    pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
    pygame.draw.line(surface, (255,255,255), (0,y), (w,y))

def redrawWindow(surface):
    global width, rows
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20 
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0),(math.floor(rows/2),math.floor(rows/2)))
    flag = True
    
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10) #cannot run more than X frames per second
    
    redrawWindow(win)
    
    pass

#rows = 
#w = 
#h = 
#
#cube.rows = rows
#cube.w = w
#
#main()
