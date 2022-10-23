import pygame
import consts

def create_screen():
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('the flag')
    screen.fill(consts.GREEN)
    pygame.display.flip()

    return screen

def run_screen():
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


import random
def create_board(board_length, board_width):
    board = []
    for row in range(board_length):
        for col in range(board_width):
            board.append("free")
    return board

def random_location_for_mines(board_width, board_length):
    random_row = random.randint(board_width)
    ranodm_col = random.randint(board_length)
    return (random_row, ranodm_col)

def spread_mines(num_of_mines, location):
    for mine in range(num_of_mines):
