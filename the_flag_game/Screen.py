def create_board(board_length, board_width):
    board = []
    for row in range(board_length):
        for col in range(board_width):
            board.append("free")
    return board