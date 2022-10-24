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
    Img = pygame.image.load(consts.FLAG_IMG)
    flagImg = pygame.transform.scale(Img, (consts.FLAG_HEIGHT, consts.FLAG_WIDTH))
    consts.SCREEN.blit(flagImg, consts.FLAG_POSITION)

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