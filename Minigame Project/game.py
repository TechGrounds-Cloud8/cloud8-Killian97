

import pygame
import config
import math
import utilities

from player import Player
from game_state import GameState
from monsterfactory import MonsterFactory

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("Havefun!!!")
        self.game_state = GameState.RUNNING

        self.load_map("01")
    
    def update(self):
        self.player_has_moved = False
        self.screen.fill(config.BLACK)
        # print("update")
        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen, self.camera)
        
        if self.player_has_moved:
            self.determine_game_events()
        
    def determine_game_events(self):
        map_tile = self.map[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_ROADNORTH:
            return
        
        if map_tile == config.MAP_TILE_ROADEAST:
            return
        
        if map_tile == config.MAP_TILE_BRIDGE:
            return
        
        if map_tile == config.MAP_TILE_CORNERUPLEFT:
            return
        
        if map_tile == config.MAP_TILE_CORNERUPRIGHT:
            return
        
        if map_tile == config.MAP_TILE_CORNERDOWNLEFT:
            return
        
        if map_tile == config.MAP_TILE_CORNERDOWNRIGHT:
            return
        
        if map_tile == config.MAP_TILE_ROADSWAP:
            return
        
        if map_tile == config.MAP_TILE_SANDROADNORTH:
            return
        
        self.determine_pokemon_found(map_tile)
    
    def determine_pokemon_found(self, map_tile):
        random_number = utilities.generate_random_number(1, 10)
        # print(random_number)

        if random_number <= 2:
            found_monster = self.monster_factory.create_monster(map_tile)
            print("Oh no you are under attack :O")
            print("Monster Type: " + found_monster.type)
            print("Monster Health: " + str(found_monster.health))
            print("Monster Attack: " + str(found_monster.attack))

            
     
    # check for key presses
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            # handling key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.NONE
                elif event.key == pygame.K_w: # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_a: # left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_s: # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_d: # right
                    self.move_unit(self.player, [1, 0])
    
    # open and read the map file (01.txt)
    def load_map(self, file_name):
        with open('C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            
            # print(self.map)
    
    def render_map(self, screen):
        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1


    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # check for edges of the map
        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return

        # check for tiles on the map where you cant walk
        if self.map[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
            return

        self.player_has_moved = True

        unit.update_position(new_position)
    

    def determine_camera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))

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