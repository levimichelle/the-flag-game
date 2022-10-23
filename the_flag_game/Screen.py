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


