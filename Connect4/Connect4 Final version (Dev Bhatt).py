def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask the user for input until they enter an input
    within a set of valid options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    user_input = ""
    while user_input not in valid_inputs:
        user_input = input(prompt)
        if user_input not in valid_inputs:
            print("Invalid input, please try again.")
        else:
            return user_input


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    board_data = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return board_data


def status(list_numb):
    if list_numb == 0:
        return "   "
    elif list_numb == 1:
        return " X "
    else:
        return " O "


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    header = "========== Connect4 =========="
    player_numb = "Player 1: X        Player 2: O"
    blank_line = ""
    numb_header = "   1   2   3   4   5   6   7  "
    row_maker = "  --- --- --- --- --- --- --- "
    bottom = "============================="

    row_1 = [0] * 7
    row_2 = [0] * 7
    row_3 = [0] * 7
    row_4 = [0] * 7
    row_5 = [0] * 7
    row_6 = [0] * 7

    for i in range(7):
        row_1[i] = status(board[0][i])
    for i in range(7):
        row_2[i] = status(board[1][i])
    for i in range(7):
        row_3[i] = status(board[2][i])
    for i in range(7):
        row_4[i] = status(board[3][i])
    for i in range(7):
        row_5[i] = status(board[4][i])
    for i in range(7):
        row_6[i] = status(board[5][i])

    column_maker_info_1 = " |" + "|".join((row_1)) + "|"
    column_maker_info_2 = " |" + "|".join((row_2)) + "|"
    column_maker_info_3 = " |" + "|".join((row_3)) + "|"
    column_maker_info_4 = " |" + "|".join((row_4)) + "|"
    column_maker_info_5 = " |" + "|".join((row_5)) + "|"
    column_maker_info_6 = " |" + "|".join((row_6)) + "|"

    print(header)
    print(player_numb)
    print(blank_line)
    print(numb_header)
    print(row_maker)
    print(column_maker_info_1)
    print(row_maker)
    print(column_maker_info_2)
    print(row_maker)
    print(column_maker_info_3)
    print(row_maker)
    print(column_maker_info_4)
    print(row_maker)
    print(column_maker_info_5)
    print(row_maker)
    print(column_maker_info_6)
    print(row_maker)
    print(bottom)
    print(blank_line)


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of the column to drop the piece into, int.
    :return: True if the piece was successfully dropped, False if not.
    """
    column_index = column - 1
    for rows in range(5, -1, -1):
        if board[rows][column_index] == 0:
            board[rows][column_index] = player
            return True

    return False


def execute_player_turn(player, board_data):
    print(f"Player {player}:")
    column = int(validate_input("Which column would you like to drop a piece into? ", ["1", "2", "3", "4", "5", "6", "7"]))
    while drop_piece(board_data, player, column) is False:
        print("That column is full, please try again.")
        column = int(validate_input("Which column would you like to drop a piece into? ", ["1", "2", "3", "4", "5", "6", "7"]))


def end_of_game(board):
    COLS = 7
    ROWS = 6

    # Check horizontal locations for a win
    for i in range(ROWS):
        for j in range(COLS - 3):
            if board[i][j] != 0 and board[i][j + 1] == board[i][j] and board[i][j + 2] == board[i][j] and board[i][j + 3] == board[i][j]:
                return board[i][j]

    # Check vertical locations for a win
    for i in range(ROWS - 3):
        for j in range(COLS):
            if board[i][j] != 0 and board[i + 1][j] == board[i][j] and board[i + 2][j] == board[i][j] and board[i + 3][j] == board[i][j]:
                return board[i][j]

    # Check positively sloped diagonals
    for i in range(ROWS - 3):
        for j in range(COLS - 3):
            if board[i][j] != 0 and board[i + 1][j + 1] == board[i][j] and board[i + 2][j + 2] == board[i][j] and board[i + 3][j + 3] == board[i][j]:
               

                return board[i][j]

    # Check negatively sloped diagonals
    for i in range(3, ROWS):
        for j in range(COLS - 3):
            if board[i][j] != 0 and board[i - 1][j + 1] == board[i][j] and board[i - 2][j + 2] == board[i][j] and board[i - 3][j + 3] == board[i][j]:
                return board[i][j]

    # Check for a tie
    if 0 not in board[0]:
        return 3

    return 0


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def local_2_player_game():
    """
    Runs a local 2-player game of Connect 4.

    :return: None
    """
    clear_screen()

    print("Welcome to Connect 4!\n")
    print("Player 1: X\nPlayer 2: O\n")
    print("Instructions:")
    print("1. Enter the column number (1-7) where you want to drop your piece.")
    print("2. Connect four pieces in a row, column, or diagonal to win!\n")

    board = create_board()
    print_board(board)

    while end_of_game(board) == 0:
        execute_player_turn(1, board)
        print_board(board)

        if end_of_game(board) != 0:
            break

        execute_player_turn(2, board)
        print_board(board)

    winner = end_of_game(board)

    if winner == 1 or winner == 2:
        print(f"Player {winner} wins! Congratulations!")
    else:
        print("It's a tie! The game is over.")


if __name__ == "__main__":
    # Run the 2-player game
    local_2_player_game()
