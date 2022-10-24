import Screen
import MineField

NUM_OF_ROWS = 25
NUM_OF_COLS = 50
screen_height = 500
screen_width = 1000
BOARD = [MineField.create_board(NUM_OF_ROWS, NUM_OF_COLS)]
SOLDIER_HEIGHT = 4
SOLDIER_WIDTH = 4
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
const_multiplication = 20
SOLDIER_Y = 0
SOLDIER_X = 0
SOLDIER_POSITION = (SOLDIER_X, SOLDIER_Y)
FLAG_POSITION = (920, 440)
BUSH_HEIGHT = BUSH_WIDTH = 3
FPS = 60
WHITE = (255, 255, 255)
start_range_of_x = SOLDIER_WIDTH * const_multiplication
stop_range_of_x = screen_width - FLAG_WIDTH * const_multiplication - BUSH_WIDTH*const_multiplication
start_range_of_y = SOLDIER_HEIGHT * const_multiplication
stop_range_of_y = screen_height - FLAG_HEIGHT * const_multiplication- BUSH_WIDTH*const_multiplication
STEP = 20
