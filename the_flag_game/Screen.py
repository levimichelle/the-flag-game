import random
def create_board(board_length, board_width):
    board = []
    for row in range(board_length):
        for col in range(board_width):
            board.append("free")
    return board

def random_location_for_mines(board_width, board_length):
    random_row = random.randint(board_width)
    ranodm_col = random.randint(board_length)
    return (random_row, ranodm_col)

def spread_mines(num_of_mines, location):
    for mine in range(num_of_mines):
