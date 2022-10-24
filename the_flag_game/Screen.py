import pygame
import consts
import random


def create_screen():
    screen = pygame.display.set_mode((consts.range_of_x, consts.range_of_y))
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

def spread_bushes(screen):
    count = 0
    while count < consts.NUM_OF_BUSHES:
        row = random.randint(consts.BOARD_WIDTH)
        col = random.randint(consts.BOARD_LENGTH)
        if consts.BOARD[row][col] == "grass":
            consts.BOARD[row][col] = "bush"
            img = pygame.image.load(consts.BUSH_IMG)
            screen.blit(img(row*consts.const_multiplication, col*consts.const_multiplication))
            count += 1

