import Screen
import MineField

BOARD_WIDTH = 25
BOARD_LENGTH = 50
BOARD = [MineField.create_board(BOARD_LENGTH, BOARD_WIDTH)]
SOLDIER_HEIGHT = 4
SOLDIER_WIDTH = 2
FLAG_HEIGHT = 3
FLAG_WIDTH = 4
MINE_HEIGHT = 1
MINE_WIDTH = 3
LOSE_MESSAGE = "You Lost!"
WIN_MESSAGE = "You Won!"
GREEN = (0, 130, 0)
BLACK = (0, 0, 0)
NUM_OF_MINES = 20
SOLDIER_IMG = "soldier.png"
BUSH_IMG = "grass.png"
FLAG_IMG = "flag.png"
MINE_IMG = "mine.png"
NUM_OF_BUSHES = 20
range_of_x = 1000
range_of_y = 500
const_multiplication = 20
SOLDIER_POSITION = (0, 0)
FLAG_POSITION = (21, 46)
BUSH_HEIGHT = 20
BUSH_WIDTH = 20
FPS = 60
SCREEN = Screen.create_screen()
