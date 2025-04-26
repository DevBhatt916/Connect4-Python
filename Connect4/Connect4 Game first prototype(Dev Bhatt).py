def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	# Implement your solution below
	user_input = ""	
	while user_input not in valid_inputs:
		user_input = input(prompt)
		if user_input not in valid_inputs:
			print("Invalid input, please try again.")
		else:
			return(user_input)
			break
			 
	#raise NotImplementedError

if __name__ == "__main__":
	# Enter test code below
	user_input = validate_input("Please select an option (a, b, c): ", ["a", "b", "c"])
    
def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	# Implement your solution below
	user_input = ""	
	while user_input not in valid_inputs:
		user_input = input(prompt)
		if user_input not in valid_inputs:
			print("Invalid input, please try again.")
		else:
			return(user_input)
			break
# Copy and paste create_board here
def create_board():
	board_data = [[0,0,0,0,0,0,0] , [0,0,0,0,0,0,0] , [0,0,0,0,0,0,0] , [0,0,0,0,0,0,0] , [0,0,0,0,0,0,0] , [0,0,0,0,0,0,0]]
	return(board_data)
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
# Copy and paste print_board here
def status(list_numb):
	if list_numb == 0:
		return("   ")
	elif list_numb == 1:
		return(" X ")
	else: 
		return(" O ") #Takes list_numb to display O or X
# VERY IMPORTANT, THE CODE FOR THE DISPLAY IS AS ABOVE. DO NOT INPUT ANY OTHER VALUE INTO list OTHER THAN 0,1,2


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Implement your solution below

	header      = "========== Connect4 =========="
	player_numb = "Player 1: X        Player 2: O"
	blank_line = ""
	numb_header = "   1   2   3   4   5   6   7  "
	row_maker   = "  --- --- --- --- --- --- --- "
	bottom      = "============================="
  # Above are the static elements of the print and below are the dynamic elements

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
 #Creating index
  # for loop??
	
	column_maker_info_1 = " |" + "|".join((row_1)) + "|"
	column_maker_info_2 = " |" + "|".join((row_2)) + "|"
	column_maker_info_3 = " |" + "|".join((row_3)) + "|"
	column_maker_info_4 = " |" + "|".join((row_4)) + "|"
	column_maker_info_5 = " |" + "|".join((row_5)) + "|"
	column_maker_info_6 = " |" + "|".join((row_6)) + "|" #joining with (|)

# Above could possibly be for looped
 
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
	# print sequence
 # Somehow for loop this aswell

# Copy and paste drop_piece here
def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	column_index = column -1
	for rows in range(5,-1,-1):
		if board[rows][column_index]==0:
			board[rows][column_index]=player
			return(True)
		
	return(False)
# Copy and paste execute_player_turn here
def execute_player_turn(player,board_data):
	print("Player", player,":")
	column = int(validate_input("Which column would you like to drop a piece into? ", ["1","2","3","4","5","6","7"]))
	while drop_piece(board_data, player, column) == False:
		print("That column is full, please try again.")
		column = int(validate_input("Which column would you like to drop a piece into? ", ["1","2","3","4","5","6","7"]))
		
	#drop_piece(board_data, player, column)
	return(column)
        
# Copy and paste end_of_game here
def end_of_game(board): # Question 6
    COLS = 7
    ROWS = 6
    for i in range(ROWS):
        for j in range(COLS -  3):
            if board[i][j] != 0 and board[i][j+1] == board[i][j] and board[i][j+2] == board[i][j] and board[i][j+3] == board[i][j]:
                return(board[i][j])
 
    # Check vertical locations for win
    for i in range(ROWS - 3):
        for j in range(COLS):
            if board[i][j] != 0 and board[i+1][j] == board[i][j] and board[i+2][j] == board[i][j] and board[i+3][j] == board[i][j]:
                return(board[i][j])
                
 
    # Check positively sloped diaganols
    for i in range(ROWS -3):
        for j in range(COLS-3):
            if board[i][j] != 0 and board[i+1][j+1] == board[i][j] and board[i+2][j+2] == board[i][j] and board[i+3][j+3] == board[i][j]:
                return(board[i][j])
    # Check negatively sloped diaganols
    for i in range(4, ROWS):
        for j in range(COLS -3):
            if board[i][j] != 0 and board[i-1][j+1] == board[i][j] and board[i-2][j+2] == board[i][j] and board[i-3][j+3] == board[i][j]:
               return(board[i][j])
    if 0 not in board[0]:
        return(3)
    return(0)

#Don't forget to include any helper functions you may have created


def clear_screen():

	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	

def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	clear_screen()
	board = create_board()
	print_board(create_board())
	end_of_game(board)
	while end_of_game(board)==0:
		execute_player_turn(1,board)
		print_board(board)
		if end_of_game(board) !=0:
			break
		execute_player_turn(2,board)
		print_board(board)
	# Implement your solution below
	#raise NotImplementedError


if __name__ == "__main__":
	# Enter test code below
	local_2_player_game()
