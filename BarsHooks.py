import pygame
import random
import sys
from tkinter import *

def generateColor():
    newColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return newColor

pygame.init()
background = pygame.image.load("Board.jpg")
backgroundRect = background.get_rect()
size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)
done = False
is_pressed = False

players = []
players.append([25, 25, 70, 70, 10, (255, 0, 0), 1, 1, 1])  # Player = [xCoord, yCoord, horizontalAdd, verticalAdd, radius, color, xIndex, yIndex, tileNum]
players.append([50, 25, 70, 70, 10, (0, 255, 0), 1, 1, 1])  # Add 70 for vertical and horizontal
players.append([25, 50, 70, 70, 10, (0, 0, 255), 1, 1, 1])  # xIndex and yIndex start with 1 para mas maganda lol
players.append([50, 50, 70, 70, 10, (255, 255, 255), 1, 1, 1])
playerTurn = 0
numPlayer = len(players)
tempCtr = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_pressed = not is_pressed
            
    if is_pressed and players[0][8] < 100 and players[1][8] < 100 and players[2][8] < 100 and players[3][8] < 100: # Check if space is pressed and no one won
        if tempCtr == 0:                    # Only 'spins' when turn is reset
            newSpin = random.randint(1, 6)
        if players[playerTurn][6] < 11:                             # Checking of yIndex
            if players[playerTurn][7] < 10:                         # Checking of xIndex
                players[playerTurn][0] += players[playerTurn][2]    # Loop constructs weren't used to illustrate movement; changes xCoord
                players[playerTurn][7] += 1                         # moves xIndex
                players[playerTurn][8] += 1                         # corrects tile number
                tempCtr += 1                                        # counter for 'loop'
            else:
                players[playerTurn][1] += players[playerTurn][3]    # changes yCoord
                players[playerTurn][2] *= -1                        # change of direction for horizontal movement through negation
                players[playerTurn][7] = 1                          # reset xIndex
                players[playerTurn][6] += 1                         # moves yIndex
                players[playerTurn][8] += 1                         # corrects tile number
                tempCtr += 1
        if tempCtr == newSpin:                                      # if loop finished, next player's turn + reset counter
            playerTurn += 1
            tempCtr = 0
        if playerTurn == numPlayer:                                 # playerTurn reset after all players made turn; simulation ends until space is pressed again
            playerTurn = 0
            is_pressed = not is_pressed

    if players[0][8] == 100:
        print("Player 1 Wins!")
    elif players[1][8] == 100:
        print("Player 2 Wins!")
    elif players[2][8] == 100:
        print("Player 3 Wins!")
    elif players[3][8] == 100:
        print("Player 4 Wins!")
        
    screen.fill((0, 0, 0))
    screen.blit(background, backgroundRect)                                                     # Something to have background image
    pygame.draw.circle(screen, players[0][5], (players[0][0], players[0][1]), players[0][4])    # Draw to the board
    pygame.draw.circle(screen, players[1][5], (players[1][0], players[1][1]), players[1][4])
    pygame.draw.circle(screen, players[2][5], (players[2][0], players[2][1]), players[2][4])
    pygame.draw.circle(screen, players[3][5], (players[3][0], players[3][1]), players[3][4])

    pygame.display.flip()
    clock.tick(120)
