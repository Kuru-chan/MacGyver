import pygame
from pygame.locals import (QUIT, K_RIGHT, K_LEFT, K_UP,
                           K_DOWN, K_ESCAPE, KEYDOWN, K_RETURN)
from classes import Maze, Character
from constants import (WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND_IMAGE,
                       MACGYVER_IMAGE, TITLE_IMAGE, HELPER_IMAGE, NEEDLE_IMAGE,
                       SYRINGE_IMAGE, TUBE_IMAGE, ETHER_IMAGE, ETHER_CHAR,
                       NEEDLE_CHAR, TUBE_CHAR, LOSE_IMAGE, WIN_IMAGE)
pygame.init()
pygame.key.set_repeat(50)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BACKGROUND = pygame.image.load(BACKGROUND_IMAGE).convert()
MACGYVER = pygame.image.load(MACGYVER_IMAGE).convert_alpha()
TITLE = pygame.image.load(TITLE_IMAGE).convert()
HELPER = pygame.image.load(HELPER_IMAGE).convert()
ETHER_I = pygame.image.load(ETHER_IMAGE).convert_alpha()
NEEDLE_I = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
SYRINGE_I = pygame.image.load(SYRINGE_IMAGE).convert_alpha()
TUBE_I = pygame.image.load(TUBE_IMAGE).convert_alpha()
LOSE = pygame.image.load(LOSE_IMAGE).convert()
WIN = pygame.image.load(WIN_IMAGE).convert()
MAIN = True
ETHER = False
NEEDLE = False
TUBE = False
while MAIN:
    WINDOW.blit(TITLE, (0, 30))
    FONT = pygame.font.Font(None, 35)
    INTRO = FONT.render("Enter to play, ESC to quit", True, (255, 255, 255))
    WINDOW.blit(INTRO, (75, 50))
    pygame.display.flip()
    GAME = True
    LOOP = True

    while LOOP:
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and \
                    event.key == K_ESCAPE:
                LOOP = False
                MAIN = False
                GAME = False
            elif event.type == KEYDOWN and event.key == K_RETURN:
                LOOP = False
        pygame.display.flip()

    MAZE = Maze()
    MAZE.display(WINDOW)
    HERO = Character(MACGYVER, MAZE)

    while GAME:
        pygame.time.Clock()
        FONT = pygame.font.Font(None, 30)
        ITEMS = FONT.render(HERO.display(), True, (255, 255, 255))
        ITEMS.fill((0, 0, 0))
        WINDOW.blit(ITEMS, (0, 5))
        ITEMS = FONT.render(HERO.display(), True, (255, 255, 255))
        WINDOW.blit(ITEMS, (0, 5))
        WINDOW.blit(BACKGROUND, (0, 30))
        MAZE.display(WINDOW)
        WINDOW.blit(HERO.macgyver, (HERO.item_x, HERO.item_y))

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and \
                    event.key == K_ESCAPE:
                GAME = False
                LOOP = False
                MAIN = False
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    HERO.movement("right")
                elif event.key == K_LEFT:
                    HERO.movement("left")
                elif event.key == K_DOWN:
                    HERO.movement("down")
                elif event.key == K_UP:
                    HERO.movement("up")

        if MAZE.structure[HERO.case_y][HERO.case_x] == ETHER_CHAR:
            HERO.delete()
            ETHER = True
            WINDOW.blit(ETHER_I, (200, 0))
        if MAZE.structure[HERO.case_y][HERO.case_x] == NEEDLE_CHAR:
            HERO.delete()
            NEEDLE = True
            WINDOW.blit(NEEDLE_I, (230, 0))
        if MAZE.structure[HERO.case_y][HERO.case_x] == TUBE_CHAR:
            HERO.delete()
            TUBE = True
            WINDOW.blit(TUBE_I, (260, 0))
        if HERO.items == 3:
            WINDOW.blit(HELPER, (200, 0))
            WINDOW.blit(SYRINGE_I, (210, 0))

        if MAZE.structure[HERO.case_y][HERO.case_x] == "a":
            if HERO.items == 3:
                WINDOW.blit(WIN, (0, 30))
                FONT = pygame.font.Font(None, 35)
                VICTORY = FONT.render("Win", True, (0, 255, 0))
                WINDOW.blit(VICTORY, (215, 225))
            else:
                if ETHER is False and NEEDLE is True and TUBE is True:
                    FONT = pygame.font.Font(None, 35)
                    DEFEAT = FONT.render("Missing ether", True, (255, 0, 0))
                elif ETHER is True and NEEDLE is False and TUBE is True:
                    FONT = pygame.font.Font(None, 35)
                    DEFEAT = FONT.render("Missing needle", True, (255, 0, 0))
                elif ETHER is True and NEEDLE is True and TUBE is False:
                    FONT = pygame.font.Font(None, 35)
                    DEFEAT = FONT.render("Missing tube", True, (255, 0, 0))
                elif ETHER is True and NEEDLE is False and TUBE is False or \
                        ETHER is False and NEEDLE is True and TUBE is False or\
                        ETHER is False and NEEDLE is False and TUBE is True:
                    FONT = pygame.font.Font(None, 35)
                    DEFEAT = FONT.render("Missing 2objects", True, (255, 0, 0))
                elif ETHER is False and NEEDLE is False and TUBE is False:
                    FONT = pygame.font.Font(None, 35)
                    DEFEAT = FONT.render("Items ?", True, (255, 0, 0))
                WINDOW.blit(LOSE, (0, 30))
                WINDOW.blit(DEFEAT, (125, 225))

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and \
                        event.key == K_ESCAPE:
                    MAIN = False
        pygame.display.flip()
