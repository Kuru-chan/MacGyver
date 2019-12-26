import os
currentFile = "constants"
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
# Maze and window caracteristics
HELPER = 30
SPRITE_SIZE = 30
SPRITE_NUM = 15
WINDOW_HEIGHT = SPRITE_NUM * SPRITE_SIZE + HELPER
WINDOW_WIDTH = SPRITE_NUM * SPRITE_SIZE
# Level file
LEVEL_FILE = dirPath + "/stage1"
# Images inside the maze
ARRIVAL_IMAGE = dirPath + "/ressources/keeper.png"
BACKGROUND_IMAGE = dirPath + "/ressources/background.png"
ETHER_IMAGE = dirPath + "/ressources/ether.png"
HELPER_IMAGE = dirPath + "/ressources/helper.png"
MACGYVER_IMAGE = dirPath + "/ressources/macgyver.png"
NEEDLE_IMAGE = dirPath + "/ressources/needle.png"
SYRINGE_IMAGE = dirPath + "/ressources/syringe.png"
TITLE_IMAGE = dirPath + "/ressources/title.png"
TUBE_IMAGE = dirPath + "/ressources/tube.png"
WALL_IMAGE = dirPath + "/ressources/wall.png"
LOSE_IMAGE = dirPath + "/ressources/lose.png"
WIN_IMAGE = dirPath + "/ressources/win.png"
# Objects designation
ETHER_CHAR = "E"
NEEDLE_CHAR = "N"
TUBE_CHAR = "T"
