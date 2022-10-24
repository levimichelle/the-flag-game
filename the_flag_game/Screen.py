import pygame
import consts
import random
import soldier
import MineField


def create_screen():
    screen = pygame.display.set_mode((consts.screen_width, consts.screen_height))
    pygame.display.set_caption('the flag')
    screen.fill(consts.GREEN)
    pygame.display.flip()
    start_text(screen)
    soldier.place_soldier(screen)
    MineField.place_flag(screen)
    spread_bushes(screen)


def spread_bushes(screen):
    lst_pos_bushes = []
    img = pygame.image.load("grass.png")
    bushImg = pygame.transform.scale(img, (consts.BUSH_WIDTH * consts.const_multiplication, consts.BUSH_HEIGHT * consts.const_multiplication))
    while len(lst_pos_bushes) < consts.NUM_OF_BUSHES:
        x = random.randint(consts.start_range_of_x, consts.stop_range_of_x)
        y = random.randint(consts.start_range_of_y, consts.stop_range_of_y)
        if (x, y) not in lst_pos_bushes:
            screen.blit(bushImg, (x, y))
            lst_pos_bushes.append((x, y))

        pygame.display.update()


def start_text(screen):
    font = pygame.font.Font('freesansbold.ttf', 12)
    text1 = font.render("Welcome to The Flag game", True, consts.WHITE)
    text2 = font.render("Have Fun!", True, consts.WHITE)
    textRect1 = text1.get_rect()
    textRect1.center = (160, 20)
    textRect2 = text2.get_rect()
    textRect2.center = (160, 40)
    # while True:
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)