import pygame
import consts
import random
import Screen
import soldier
import MineField


def create_screen():
    screen = pygame.display.set_mode((consts.range_of_x, consts.range_of_y))
    pygame.display.set_caption('the flag')
    screen.fill(consts.GREEN)
    pygame.display.flip()
    start_text(screen)
    soldier.place_soldier(screen)
    MineField.place_flag(screen)
    spread_bushes(screen)



def spread_bushes(screen):
    count = 0
    while count < consts.NUM_OF_BUSHES:
        row = random.randint(0, consts.BOARD_WIDTH)
        col = random.randint(0, consts.BOARD_LENGTH)
        if MineField.board_matrix[row][col] == "grass":
            consts.BOARD[row][col] = "bush"
        img = pygame.image.load("grass.png")
        bushImg = pygame.transform.scale(img, (consts.BUSH_WIDTH*consts.const_multiplication, consts.BUSH_HEIGHT*consts.const_multiplication))
        screen.blit(bushImg, (row * consts.const_multiplication, col * consts.const_multiplication))
        pygame.display.update()
        count += 1


def start_text(screen):
    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render("Welcome to The Flag game \n Have Fun! ", True, consts.WHITE)
    textRect = text.get_rect()
    textRect.center = (60, 20)
    while True:
        screen.blit(text, textRect)