# import pygame library
import pygame
# import config.py
import config
#import gamestate class from game_state.py
from game_state import GameState


# import class Game from game.py
from game import Game

from menu import Menu

# Initialize pygame
pygame.init()

# Create window and define Size
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

# Give title to window
pygame.display.set_caption("Pokemon")

# set var for framerate
clock = pygame.time.Clock()

# game var is equal to the Class "Game" on screen
game = Game(screen)

# sets up the game and the screen
# game.set_up()

menu = Menu(screen, game)
menu.set_up()

# allows the game to be running and also quitting
while game.game_state != GameState.ENDED:
    # set framerate
    clock.tick(50)
    
    if game.game_state == GameState.NONE:
        menu.update()
    
    if game.game_state == GameState.RUNNING:    
        game.update()
    
    # Update the full display Surface to the screen
    pygame.display.flip()
