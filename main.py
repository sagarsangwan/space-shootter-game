from math import e
import pygame
import random

# starting pygame
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("spaceship invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")

# player
playerimage = pygame.image.load("spaceship (2).png")
playerx = 400
playery = 530
playerx_change = 0
playery_change = 0

# enemy
enemyimage = pygame.image.load("enemy.png")
enemyx = random.randint(100, 700)
enemyy = random.randint(50, 100)
enemyx_change = 0.3
enemyy_change = 0.3


def player(x, y):
    screen.blit(playerimage, (x, y))


def enemy(x, y):
    screen.blit(enemyimage, (x, y))


# game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerx_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerx_change = +0.7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    enemyx += enemyx_change
    enemyy += enemyy_change

    if enemyx <= 0:
        enemyx = 0
        enemyy += 50
        enemyx_change = +0.5

    elif enemyx >= 736:
        enemyy += 50

        enemyx_change = -0.5

    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()
