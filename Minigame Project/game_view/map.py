

import pygame
import config
import math
import utilities

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]

    # open and read the map file (01.txt)
    def load(self, file_name):
        with open('C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            # print(self.map_array)
    
    def render(self, screen, player, objects):
        self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1
        
        for object in objects:
            object.render(self.screen, self.camera)

    
    def determine_camera(self, player):
        max_y_position = len(self.map_array) - config.SCREEN_HEIGHT / config.SCALE
        y_position = player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position


map_tile_image = {
   config.MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/grass1.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_WATER : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/water1.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_ROADNORTH : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/roadnorth.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_ROADEAST : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/roadeast.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_CORNERDOWNRIGHT : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/cornerdownright.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_CORNERDOWNLEFT : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/cornerdownleft.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_CORNERUPRIGHT : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/cornerupright.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_CORNERUPLEFT : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/cornerupleft.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_BRIDGE : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/bridge.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_SAND : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/sand1.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_GROUNDSWAP : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/groundswap.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_ROADSWAP : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/roadswap.png"), (config.SCALE, config.SCALE)),
   config.MAP_TILE_SANDROADNORTH : pygame.transform.scale(pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/sandroadnorth.png"), (config.SCALE, config.SCALE))
}