import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_SPEED_X_MAX = 150
ENEMY_SPEED_x = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Inialize Pygame
pygame.init()

# Creat the screen
screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("space Invader")
icon = pygame.imag.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_Change = 0

#  Enemy 
enemyImg =  []
enemyX = [] 
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyY_change.append( )