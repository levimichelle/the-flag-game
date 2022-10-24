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
    Screen.create_screen()

    while state["is window open"]:
        handle_user_events()
        soldier.soldier_moving()


def handle_user_events():
    while state["is window open"]:
        for event in pygame.event.get():
            clock = pygame.time.Clock()
            clock.tick(60)

            if event.type == pygame.QUIT:
                state["is window open"] = False


if __name__ == '__main__':
    main()