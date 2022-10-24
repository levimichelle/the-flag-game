import consts
import MineField
import pygame
import Screen
import soldier

state = {
    "is window open": True,
    "is soldier moving": True,
    }


def main():
    pygame.init()
    consts.SCREEN

    while state["is window open"]:
        handle_user_events()
            # Screen.spread_bushes(screen)
        soldier.place_soldier()
        pygame.display.update()
        MineField.place_flag()


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
    while state["is window open"]:
        clock = pygame.time.Clock()
        clock.tick(consts.FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state["is window open"] = False

    pygame.display.update()




if __name__ == '__main__':
    main()