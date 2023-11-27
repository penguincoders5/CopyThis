
#Main.Py
import pygame, sys
from Fruit import Fruit

pygame.init()

BG_COLOR = (234, 212, 252)
SIZE = (500, 500)
FLOOR = 450

screen = pygame.display.set_mode(SIZE)
screen.fill(BG_COLOR)

pygame.display.flip()
import random

running = True
elements = []
while running:
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (0, 255, 150), pygame.Rect(0, FLOOR, 500, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            elements.append(Fruit(screen, pos, 1))

    toremove = []
    for i in range(len(elements)):
        for j in range(len(elements)):
            if i != j:
                if elements[i].ballCollision(elements[j]):
                    toremove.append(j)
    for i in range(len(elements)):
        if i in toremove:
            elements.pop(i)
    for f in elements:
        f.update()


    pygame.time.wait(1)

    pygame.display.update()


