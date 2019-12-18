import os, pygame, random
from constants import LEVEL_FILE, ETHER_CHAR, NEEDLE_CHAR, TUBE_CHAR, ARRIVAL_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE, TUBE_IMAGE, WALL_IMAGE, SPRITE_SIZE, SPRITE_NUM, HELPER
currentFile = "classes"

class Maze:
    def __init__(self):
        self.items = 0
        self.structure = self.generate()

    def generate(self):
        with open(LEVEL_FILE, 'r') as f:
            structure = []
            for line in f:
                line_m = []
                for letter in line:
                    if letter != '\n':
                        line_m.append(letter)
                structure.append(line_m)

        while self.items < 3:
            item_x = random.randint(0, 14)
            item_y = random.randint(0, 14)
            if item_x and item_y == 0 or item_x and item_y == 14:
                item_x = random.randint(0, 14)
                item_y = random.randint(0, 14)

            if structure[item_y][item_x] == "0":
                if self.items == 0:
                    structure[item_y][item_x] = ETHER_CHAR
                elif self.items == 1:
                    structure[item_y][item_x] = NEEDLE_CHAR
                elif self.items == 2:
                    structure[item_y][item_x] = TUBE_CHAR

                self.items += 1

        return structure

    def display(self, window):
        arrival = pygame.image.load(ARRIVAL_IMAGE).convert_alpha()
        ether = pygame.image.load(ETHER_IMAGE).convert_alpha()
        needle = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
        tube = pygame.image.load(TUBE_IMAGE).convert_alpha()
        wall = pygame.image.load(WALL_IMAGE).convert()

        line_n = 0
        for line in self.structure:
            case_n = 0
            for sprite in line:
                pos_x = case_n * SPRITE_SIZE
                pos_y = line_n * SPRITE_SIZE + HELPER
                if sprite == "m":
                    window.blit(wall, (pos_x, pos_y))
                elif sprite == "a":
                    window.blit(arrival, (pos_x, pos_y))
                elif sprite == ETHER_CHAR:
                    window.blit(ether, (pos_x, pos_y))
                elif sprite == NEEDLE_CHAR:
                    window.blit(needle, (pos_x, pos_y))
                elif sprite == TUBE_CHAR:
                    window.blit(tube, (pos_x, pos_y))
                case_n += 1
            line_n +=1

class Character:
    def __init__(self, macgyver, maze):
        self.macgyver = macgyver
        self.maze = maze
        self.item_x = 0
        self.item_y = 30
        self.case_x = 0
        self.case_y = 0
        self.items = 0

    def movement(self, direction):
        if direction == "right":
            if self.case_x < (SPRITE_NUM - 1):
                if self.maze.structure[self.case_y][self.case_x + 1] != "m":
                    self.case_x += 1
                    self.item_x = self.case_x * SPRITE_SIZE
        elif direction == "left":
            if self.case_x > 0:
                if self.maze.structure[self.case_y][self.case_x - 1] != "m":
                    self.case_x -= 1
                    self.item_x = self.case_x * SPRITE_SIZE
        elif direction == "up":
            if self.case_y > 0:
                if self.maze.structure[self.case_y - 1][self.case_x] != "m":
                    self.case_y -= 1
                    self.item_y = self.case_y * SPRITE_SIZE + HELPER
        elif direction == "down":
            if self.case_y < (SPRITE_NUM - 1):
                if self.maze.structure[self.case_y + 1][self.case_x] != "m":
                    self.case_y += 1
                    self.item_y = self.case_y * SPRITE_SIZE + HELPER

    def delete(self):
        self.maze.structure[self.case_y][self.case_x] = "0"
        self.items += 1

    def display(self):
        objective = f"Remaining items: {3- self.items}"
        return objective