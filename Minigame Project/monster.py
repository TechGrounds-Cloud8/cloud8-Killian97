

import pygame


class Monster:
    def __init__(self, monster_type,  id):
        print("Monster created")
        self.type = monster_type
        self.health = 10
        self.attack = 10
        self.id = id

        if monster_type == "G":
            self.image = pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/monsters/grass/" + f"{self.id:03d}" + ".png")
        elif monster_type == "S":
            self.image = pygame.image.load("C:/Users/Lenovo/Documents/GitHub/cloud8-Killian97/Minigame Project/imgs/monsters/sand/" + f"{self.id:03d}" + ".png")

