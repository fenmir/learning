# 1 - import packages
import pygame
from pygame.locals import * 
import sys 

from pathlib import Path

import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT


BASE_PATH = Path('anime girl.png')

#pathToBall = BASE_PATH + 'images/ball.png'

# 3 - Initailize the world 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: iamge(s), sound(s), etc.
ballImage = pygame.image.load('anime girl.png')

# 5 - Initalize variables 
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# 6 - Loop forever 
while True: 

    # 7 - Check for and hanle events 
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos # Could do this if we needed it

            # Check if the clik was in the rect of the ball
            # If so, choose a random new location
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, 
                                       BALL_WIDTH_HEIGHT, 
                                       BALL_WIDTH_HEIGHT
                                       )
    # 8 - Do any "per frame" actions 
            
    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements 
    window.blit(ballImage, (ballX, ballY))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit 
    clock.tick(FRAMES_PER_SECOND)








