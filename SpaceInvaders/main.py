''' Following this tutorial from FreeCodeCamp 
https://www.youtube.com/watch?v=FfWpgLFMI7w&list=PLdwezzyF4RX3-j51DIiDd_0pwNPisbe_4&index=2&t=1s&ab_channel=freeCodeCamp.org '''

import pygame
import random

# Initialize pygame
pygame.init()

# Create the screen
infoObject = pygame.display.Info()
screenX = infoObject.current_w/1.25
screenY = infoObject.current_h/1.25
screen = pygame.display.set_mode((screenX, screenY))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("ship.png")
playerX = screenX/2
playerY = screenY/1.2
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, int(screenX))
enemyY = random.randint(int(screenY//10), int(screenY//4))
enemyX_change = 0.5

# Laser
laserImg = pygame.image.load("laser.png")
laserX = playerX
laserY = playerY
laserY_change = -15
laser_active = False

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def laser(x, y):
    global laser_active
    laser_active = True
    screen.blit(laserImg, (x, y))

# Game loop
running = True
while running:
    screen.fill((25, 25, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            elif event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE and not laser_active:
                laserX = playerX
                laserY = playerY
                laser(laserX, laserY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= screenX - 64:
        playerX = screenX - 64

    enemyX += enemyX_change
    enemyY += .15

    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 0.5
    elif enemyX >= screenX - 64:
        enemyX = screenX - 64
        enemyX_change = -0.5

    if int(enemyY) == int(playerY):
        print("Enemy has passed!")

    if laser_active:
        laserY += laserY_change
        laser(laserX, laserY)

        if laserY <= 0:
            laser_active = False

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()