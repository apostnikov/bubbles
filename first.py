#! /usr/bin/env python

import pygame
import random

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    x = random.randint(1,640)
    y = random.randint(1,480)
    z = random.randint(1,100)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    for j in range (z):
        pygame.draw.circle(screen,[r,g,b],[x,y],j,0)
        pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()