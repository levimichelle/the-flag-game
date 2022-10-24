import pygame
import consts
import random
import Screen


def create_screen():
    screen = pygame.display.set_mode((consts.range_of_x, consts.range_of_y))
    pygame.display.set_caption('the flag')
    screen.fill(consts.GREEN)
    pygame.display.flip()



def spread_bushes(screen):
    count = 0
    while count < consts.NUM_OF_BUSHES:
        row = random.randint(0, consts.BOARD_WIDTH)
        col = random.randint(0, consts.BOARD_LENGTH)
        if consts.BOARD[row][col] == "grass":
            consts.BOARD[row][col] = "bush"
            img = pygame.image.load(consts.BUSH_IMG)
            bushImg = pygame.transform.scale(img, (consts.BUSH_WIDTH, col * consts.BUSH_HEIGHT))
            Screen.create_screen.blit(bushImg, (row * consts.const_multiplication, col * consts.const_multiplication))
            count += 1


