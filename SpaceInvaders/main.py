''' Roughly following this tutorial from FreeCodeCamp 
https://www.youtube.com/watch?v=FfWpgLFMI7w&list=PLdwezzyF4RX3-j51DIiDd_0pwNPisbe_4&index=2&t=1s&ab_channel=freeCodeCamp.org '''

import pygame
import random
import math
import time

# Initialize pygame
pygame.init()

# Create the screen
infoObject = pygame.display.Info()
screenX = 800
screenY = 800
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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

def genEnemyX():
    return random.randint(0, int(screenX))

def genEnemyY():
    return random.randint(int(screenY//10), int(screenY//4))

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(genEnemyX())
    enemyY.append(genEnemyY())
    if random.randint(1,2) == 1:
        enemyX_change.append(1)
    else:
        enemyX_change.append(-1)
    enemyY_change.append(0.5)

# Laser
laserImg = pygame.image.load("laser.png")
laserX = playerX
laserY = playerY
laserY_change = -25
laser_active = False

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10

def show_score():
    global scoreX, scoreY
    scoreboard = font.render("Score: " + str(score), 
                             True, 
                             (255, 255, 255))
    screen.blit(scoreboard, (scoreX, scoreY))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def laser(x, y):
    global laser_active
    laser_active = True
    screen.blit(laserImg, (x, y))

def isColliding(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt(math.pow(enemyX-laserX,2) + math.pow(enemyY-laserY,2))
    if distance < 27:
        return True
    else:
        return False

def resetEnemy(i):
    enemyX[i] = genEnemyX()
    enemyY[i] = genEnemyY()

def showGameOver():
    gameover_text = font.render("GAME OVER!", 
                                True, 
                                (255, 255, 255))
    screen.blit(gameover_text, (400, 400))

# Game loop
running = True
while running:
    screen.fill((25, 25, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -6
            elif event.key == pygame.K_RIGHT:
                playerX_change = 6
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

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]

        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 1.5
        elif enemyX[i] >= screenX - 64:
            enemyX[i] = screenX - 64
            enemyX_change[i] = -1.5

        if int(enemyY[i]) >= int(playerY):
            print("Enemy has passed!")
            score -= 500
            print(score)
            enemyY[i] = genEnemyY()

        if isColliding(enemyX[i], enemyY[i], laserX, laserY):
            laser_active = False
            laserY = playerY
            score += 100
            print(score)
            resetEnemy(i)


        enemy(enemyX[i], enemyY[i], i)

    if laser_active:
        laserY += laserY_change
        laser(laserX, laserY)

        if laserY <= 0:
            laser_active = False

    if score < 0:
        showGameOver()
        pygame.display.update()
        time.sleep(3)
        running = False

    player(playerX, playerY)
    show_score()
    pygame.display.update()