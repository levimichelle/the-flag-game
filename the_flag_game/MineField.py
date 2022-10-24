import pygame

import Screen
import consts
import random


def create_board(board_length, board_width):
    board = []
    for row in range(board_length):
        new_row = []
        for col in range(board_width):
            new_row.append("grass")
        board.append(new_row)
    return board


def place_flag(screen):
    Img = pygame.image.load('flag.png')
    flagImg = pygame.transform.scale(Img, ( consts.FLAG_WIDTH*consts.const_multiplication, consts.FLAG_HEIGHT*consts.const_multiplication))
    screen.blit(flagImg, consts.FLAG_POSITION)
    pygame.display.update()

# board_matrix = consts.BOARD.copy()
# board_matrix[21][46] = "flag"
# board_matrix[22][46] = "flag"
# board_matrix[23][46] = "flag"
# board_matrix[21][47] = "flag"
# board_matrix[22][47] = "flag"
# board_matrix[23][47] = "flag"
# board_matrix[21][48] = "flag"
# board_matrix[22][48] = "flag"
# board_matrix[23][48] = "flag"


# def spread_mines():
#     count = 0
#     while count < consts.NUM_OF_MINES:
#         row = random.randint(consts.BOARD_WIDTH)
#         col = random.randint(consts.BOARD_LENGTH)
#     if :
#         consts.BOARD[row][col] = "mine"
#         count += 1