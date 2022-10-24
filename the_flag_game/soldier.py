import pygame
import Screen
import consts



def place_soldier():
    Img = pygame.image.load('soldier.png')
    soldierImg = pygame.transform.scale(Img, (consts.SOLDIER_WIDTH, consts.SOLDIER_WIDTH))
    consts.SCREEN.blit(soldierImg, consts.SOLDIER_POSITION)
    pygame.display.update()






