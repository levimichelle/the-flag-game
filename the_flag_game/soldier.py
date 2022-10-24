import pygame
import Screen
import consts



def place_soldier(screen):
    Img = pygame.image.load('soldier.png')
    soldierImg = pygame.transform.scale(Img, (consts.SOLDIER_WIDTH*consts.const_multiplication, consts.SOLDIER_WIDTH*consts.const_multiplication))
    screen.blit(soldierImg, consts.SOLDIER_POSITION)
    pygame.display.update()






