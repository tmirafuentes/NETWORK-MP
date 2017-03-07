import pygame
import random
import sys
from tkinter import *

def generateColor():
    newColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return newColor

class Spinner:
    def getSpin(self):
        newSpin = random.randint(1,6)
        return newSpin

    def checkBoH(self,playerNum, position):
        if position == 4 :
            print('Player', playerNum, 'Bar from 4 to 14')
            return 14
        elif position == 9 :
            print('Player', playerNum, 'Bar from 9 to 31')
            return 31
        elif position == 20 :
            print('Player', playerNum, 'Bar from 20 to 38')
            return 38
        elif position == 28 :
            print('Player', playerNum, 'Bar from 28 to 84')
            return 84
        elif position == 40 :
            print('Player', playerNum, 'Bar from 40 to 59')
            return 59
        elif position == 51 :
            print('Player', playerNum, 'Bar from 51 to 68')
            return 68
        elif position == 63 :
            print('Player', playerNum, 'Bar from 63 to 81')
            return 81
        elif position == 71 :
            print('Player', playerNum, 'Bar from 71 to 91')
            return 91
        elif position == 17 :
            print('Player', playerNum, 'Hook from 17 to 7')
            return 7
        elif position == 62 :
            print('Player', playerNum, 'Hook from 62 to 19')
            return 19
        elif position == 64 :
            print('Player', playerNum, 'Hook from 64 to 60')
            return 60
        elif position == 54 :
            print('Player', playerNum, 'Hook from 54 to 34')
            return 34
        elif position == 87 :
            print('Player', playerNum, 'Hook from 87 to 24')
            return 24
        elif position == 93 :
            print('Player', playerNum, 'Hook from 93 to 73')
            return 73
        elif position == 99 :
            print('Player', playerNum, 'Hook from 99 to 78')
            return 78
        elif position == 93 :
            print('Player', playerNum, 'Hook from 93 to 73')
            return 73
        else:
            return position

spin = Spinner()

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
printed = False
BoH = False
move = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_pressed = not is_pressed
 
    if is_pressed and players[0][8] < 100 and players[1][8] < 100 and players[2][8] < 100 and players[3][8] < 100: # Check if space is pressed and no one won
        if tempCtr == 0 and not BoH:                                            # Only 'spins' when turn is reset
            rollDie = spin.getSpin()
        if players[playerTurn][7] < 11 and not BoH:                             # Checking of yIndex
            if players[playerTurn][6] < 10:                         # Checking of xIndex
                players[playerTurn][0] += players[playerTurn][2]    # Loop constructs weren't used to illustrate movement; changes xCoord
                players[playerTurn][6] += 1                         # moves xIndex
                players[playerTurn][8] += 1                         # corrects tile number
                tempCtr += 1                                        # counter for 'loop'
            else:
                players[playerTurn][1] += players[playerTurn][3]    # changes yCoord
                players[playerTurn][2] *= -1                        # change of direction for horizontal movement through negation
                players[playerTurn][6] = 1                          # reset xIndex
                players[playerTurn][7] += 1                         # moves yIndex
                players[playerTurn][8] += 1                         # corrects tile number
                tempCtr += 1
        elif BoH:
            # New Coordinates
            if move % 10 != 0:
                yNew = (move // 10) + 1
            else:
                yNew = move // 10
                
            if yNew % 2 == 0:
                if move % 10 != 0:
                    xNew = 11 - (move % 10)
                else:
                    xNew = 1
            else:
                if move % 10 == 0:
                    xNew = 10
                else:
                    xNew = move % 10
            # Current Coordinates    
            if (players[playerTurn][8] % 10 != 0):
                yCurr = (players[playerTurn][8] // 10) + 1
            else:
                yCurr = (players[playerTurn][8] // 10)
                
            if (yCurr % 2) == 0:
                if players[playerTurn][8] % 10 != 0:
                    xCurr = 11 - (players[playerTurn][8] % 10)
                else:
                    xCurr = 1
            else:
                if (players[playerTurn][8] % 10 == 0):
                    xCurr = 10
                else:
                    xCurr = (players[playerTurn][8] % 10)
                    
            # Distance and Updating    
            yDist = yNew - yCurr
            xDist = xNew - xCurr
            players[playerTurn][8] = move
            players[playerTurn][0] += (xDist * 70)
            players[playerTurn][1] += (yDist * 70)
            players[playerTurn][7] = yNew
            if (yNew % 2 == 0):
                if players[playerTurn][2] == 70:
                    players[playerTurn][2] = -70
                players[playerTurn][6] = (11 - xNew)
            else:
                if players[playerTurn][2] == -70:
                    players[playerTurn][2] = 70
                players[playerTurn][6] = xNew
            corrected = 0
            
        if tempCtr == rollDie and not BoH:                                      # if loop finished, next player's turn + reset counter
            print("Player", playerTurn+1, "rolls a", str(rollDie))
            move = spin.checkBoH(playerTurn+1, players[playerTurn][8])
            if move == players[playerTurn][8]:
                playerTurn += 1
                is_pressed = not is_pressed
            else:
                BoH = True
            tempCtr = 0

        elif BoH:
            playerTurn += 1
            is_pressed = not is_pressed
            BoH = False
        if playerTurn == numPlayer:                                 # playerTurn reset after all players made turn; simulation ends until space is pressed again
            playerTurn = 0

    if players[0][8] == 100 and not printed:
        print("Player 1 Wins!")
        printed = not printed
    elif players[1][8] == 100 and not printed:
        print("Player 2 Wins!")
        printed = not printed
    elif players[2][8] == 100 and not printed:
        print("Player 3 Wins!")
        printed = not printed
    elif players[3][8] == 100 and not printed:
        print("Player 4 Wins!")
        printed = not printed
        
    #screen.fill((0, 0, 0))
    screen.blit(background, backgroundRect)                                                     # Something to have background image
    pygame.draw.circle(screen, players[0][5], (players[0][0], players[0][1]), players[0][4])    # Draw to the board
    pygame.draw.circle(screen, players[1][5], (players[1][0], players[1][1]), players[1][4])
    pygame.draw.circle(screen, players[2][5], (players[2][0], players[2][1]), players[2][4])
    pygame.draw.circle(screen, players[3][5], (players[3][0], players[3][1]), players[3][4])

    pygame.display.flip()
    clock.tick(120)
