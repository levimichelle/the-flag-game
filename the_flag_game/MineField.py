import consts

board_matrix = consts.BOARD.copy()
board_matrix[21][46] = "flag"
board_matrix[22][46] = "flag"
board_matrix[23][46] = "flag"
board_matrix[21][47] = "flag"
board_matrix[22][47] = "flag"
board_matrix[23][47] = "flag"
board_matrix[21][48] = "flag"
board_matrix[22][48] = "flag"
board_matrix[23][48] = "flag"





def spread_mines():
    count = 0
    while count < consts.NUM_OF_MINES:
        row = random.randint(consts.BOARD_WIDTH)
        col = random.randint(consts.BOARD_LENGTH)
    if :
        consts.BOARD[row][col] = "mine"
        count += 1