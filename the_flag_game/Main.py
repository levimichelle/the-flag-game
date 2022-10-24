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
    while state["is window open"]:
        handle_user_events()


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
def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is window open"]= False




if __name__ == '__main__':
    main()