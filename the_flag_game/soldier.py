import pygame
import consts


def place_soldier(screen):
    Img = pygame.image.load('soldier.png')
    soldierImg = pygame.transform.scale(Img, (
    consts.SOLDIER_WIDTH * consts.const_multiplication, consts.SOLDIER_HEIGHT * consts.const_multiplication))
    screen.blit(soldierImg, consts.SOLDIER_POSITION)
    pygame.display.update()


def soldier_moving(screen):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        consts.SOLDIER_Y -= consts.STEP
    if pressed[pygame.K_DOWN]:
        consts.SOLDIER_Y += consts.STEP
    if pressed[pygame.K_LEFT]:
        consts.SOLDIER_X -= consts.STEP
    if pressed[pygame.K_RIGHT]:
        consts.SOLDIER_X += consts.STEP

    Img = pygame.image.load('soldier.png')
    soldierImg = pygame.transform.scale(Img, (
    consts.SOLDIER_WIDTH * consts.const_multiplication, consts.SOLDIER_HEIGHT * consts.const_multiplication))
    screen.blit((soldierImg, consts.SOLDIER_POSITION))
    pygame.display.update()
