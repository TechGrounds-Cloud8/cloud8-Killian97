

import pygame
import config
import math
import utilities

from player import Player
from game_state import GameState, CurrentGameState
from monsterfactory import MonsterFactory
from game_view.map import Map

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()
        self.map = Map(screen)

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("Havefun!!!")
        self.game_state = GameState.RUNNING

        self.map.load("01")
    
    def update(self):
        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.screen.fill(config.BLACK)
            # print("update")
            self.handle_events()

            self.map.render(self.screen, self.player, self.objects)
            
            if self.player_has_moved:
                self.determine_game_events()
        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
        
    def determine_game_events(self):
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]]
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


    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # check for edges of the map
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return

        # check for tiles on the map where you cant walk
        if self.map.map_array[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
            return

        self.player_has_moved = True

        unit.update_position(new_position)  


