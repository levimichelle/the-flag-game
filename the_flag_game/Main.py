import consts
import MineField
import pygame
import Screen
import soldier

state = {
    "is window open" : True,
    "is soldier moving" : True,
    }


def main():
    pygame.init()
    screen = Screen.create_screen()
    Screen.spread_bushes(screen)
    # while state["is window open"]:


# board = []
# for row in range(consts.BOARD_LENGTH):
#     new_row = []
#     for col in range(consts.BOARD_WIDTH):
#         new_row.append("grass")
#     board.append(new_row)
#
# for row in board:
#     for col in row:
#         print(col, end=" ")
#     print()
# print(board)

if __name__ == '__main__':
    main()