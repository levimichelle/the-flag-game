import consts
import MineField
import pygame
import Screen
import soldier

state = {
    "is window open" : True,
    "is soldier moving" : True,
    ""
}
def main():
    while "is window open":
        pygame.init()
        Screen.create_board()

