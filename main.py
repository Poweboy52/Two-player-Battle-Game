import pygame
from pygame.locals import *
import os
import math
import sys

x = 80
y = 25
Enemy_x = 1400
Enemy_y = 640
MR = 4
FPSCLOCK = pygame.time.Clock()
pygame.init()
FPS = 60
DISPLAYSURF = pygame.display.set_mode((1500, 760))
moveDown = False
moveUp = False
moveLeft = False
moveRight = False
moveDown2 = False
moveUp2 = False
moveLeft2 = False
moveRight2 = False
MAXHEALTH = 5
currentHealth = MAXHEALTH
invincible = 0
time = 0
on_enemy = 0
MAXHEALTH2 = 5
currentHealth2 = MAXHEALTH2
BASICFONT = pygame.font.Font('freesansbold.ttf', 32)


def terminate():
    pygame.quit()
    sys.exit()


def main(x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x, Enemy_y,
         currentHealth, MAXHEALTH, invincible, time, on_enemy, BASICFONT, MR, currentHealth2, MAXHEALTH2):
    if x >= Enemy_x - 60 and x + 60 <= Enemy_x + 120 and y >= Enemy_y - 60 and y + 60 <= Enemy_y + 120:
        if invincible == 0:
            if ((time * 0.03) % 2) < 1:
                currentHealth -= 1
            else:
                currentHealth2 -= 1
            MR *= 1.2
        else:
            on_enemy += 1
            if on_enemy >= 75:
                on_enemy = 0
                invincible = 1
                if ((time * 0.03) % 2) < 1:
                    currentHealth -= 1
                else:
                    currentHealth2 -= 1
                MR *= 1.2
        invincible = 1
    else:
        invincible = 0
        on_enemy = 0
    time += 0.05
    winSurf = BASICFONT.render(str(int(time * 20 / 60) * 100), True, (255, 255, 255))
    winRect = winSurf.get_rect()
    winRect.center = (750, 50)
    colour = (255, 255, 0)
    pygame.draw.rect(DISPLAYSURF, (0, 0, 255), pygame.Rect(0, 0, 2000, 2000))
    (x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x, Enemy_y,
     MR) = move(x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x,
                Enemy_y, MR)
    if ((time * 0.03) % 2) < 1:
        pygame.draw.rect(DISPLAYSURF, colour, pygame.Rect(x, y, 60, 60))
        pygame.draw.rect(DISPLAYSURF, (255, 64, 64), pygame.Rect(Enemy_x, Enemy_y, 60, 60))
    else:
        pygame.draw.rect(DISPLAYSURF, colour, pygame.Rect(Enemy_x, Enemy_y, 60, 60))
        pygame.draw.rect(DISPLAYSURF, (255, 64, 64), pygame.Rect(x, y, 60, 60))
    for i in range(currentHealth):
        pygame.draw.rect(DISPLAYSURF, (255, 64, 64), (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10))
    for i in range(MAXHEALTH):
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10), 1)
    for i in range(currentHealth2):
        pygame.draw.rect(DISPLAYSURF, (255, 64, 64), (1460, 5 + (10 * MAXHEALTH2) - i * 10, 20, 10))
    for i in range(MAXHEALTH2):
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (1460, 5 + (10 * MAXHEALTH2) - i * 10, 20, 10), 1)
        DISPLAYSURF.blit(winSurf, winRect)
    pygame.display.update()
    return (x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x, Enemy_y,
            currentHealth, MAXHEALTH, invincible, time, on_enemy, BASICFONT, MR, currentHealth2, MAXHEALTH2)


def move(x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x, Enemy_y, MR):
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key in (K_w, K_UP):
                moveDown = False
                moveUp = True
            elif event.key in (K_s, K_DOWN):
                moveUp = False
                moveDown = True
            elif event.key in (K_a, K_LEFT):
                moveRight = False
                moveLeft = True
            elif event.key in (K_d, K_RIGHT):
                moveLeft = False
                moveRight = True
            elif event.key in (K_i, K_UP):
                moveDown = False
                moveUp2 = True
            elif event.key in (K_k, K_UP):
                moveUp2 = False
                moveDown2 = True
            elif event.key in (K_j, K_UP):
                moveRight2 = False
                moveLeft2 = True
            elif event.key in (K_l, K_UP):
                moveLeft2 = False
                moveRight2 = True
        if event.type == KEYUP:
            if event.key in (K_a, K_LEFT):
                moveLeft = False
            elif event.key in (K_d, K_RIGHT):
                moveRight = False
            elif event.key in (K_w, K_UP):
                moveUp = False
            elif event.key in (K_s, K_DOWN):
                moveDown = False
            elif event.key in (K_j, K_UP):
                moveLeft2 = False
            elif event.key in (K_l, K_UP):
                moveRight2 = False
            elif event.key in (K_i, K_DOWN):
                moveUp2 = False
            elif event.key in (K_k, K_UP):
                moveDown2 = False
    if ((time * 0.03) % 2) < 1:
        MR3 = int(float(MR) * 1.2)
        MR2 = MR
    else:
        MR2 = int(1.2 * float(MR))
        MR3 = MR
    if moveLeft == True:
        x -= MR3
        if x <= 0:
            x = 0
    if moveRight == True:
        x += MR3
        if x + 60 >= 1500:
            x = 1440
    if moveDown == True:
        y += MR3
        if y + 60 >= 760:
            y = 700
    if moveUp == True:
        y -= MR3
        if y <= 0:
            y = 0
    if moveLeft2 == True:
        Enemy_x -= MR2
        if Enemy_x <= 0:
            Enemy_x = 0
    if moveRight2 == True:
        Enemy_x += MR2
        if Enemy_x + 60 >= 1500:
            Enemy_x = 1440
    if moveDown2 == True:
        Enemy_y += MR2
        if Enemy_y + 60 >= 760:
            Enemy_y = 700
    if moveUp2 == True:
        Enemy_y -= MR2
        if Enemy_y <= 0:
            Enemy_y = 0
    return (
    x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x, Enemy_y, MR)


while True:
    if __name__ == '__main__':
        if currentHealth < 1:
            terminate()
        if currentHealth2 < 1:
            terminate()
        (x, y, moveDown, moveUp, moveLeft, moveRight, moveDown2, moveUp2, moveLeft2, moveRight2, Enemy_x, Enemy_y,
         currentHealth, MAXHEALTH, invincible, time, on_enemy, BASICFONT, MR, currentHealth2, MAXHEALTH2) = main(x, y,
                                                                                                                 moveDown,
                                                                                                                 moveUp,
                                                                                                                 moveLeft,
                                                                                                                 moveRight,
                                                                                                                 moveDown2,
                                                                                                                 moveUp2,
                                                                                                                 moveLeft2,
                                                                                                                 moveRight2,
                                                                                                                 Enemy_x,
                                                                                                                 Enemy_y,
                                                                                                                 currentHealth,
                                                                                                                 MAXHEALTH,
                                                                                                                 invincible,
                                                                                                                 time,
                                                                                                                 on_enemy,
                                                                                                                 BASICFONT,
                                                                                                                 MR,
                                                                                                                 currentHealth2,
                                                                                                                 MAXHEALTH2)
        FPSCLOCK.tick(FPS)
