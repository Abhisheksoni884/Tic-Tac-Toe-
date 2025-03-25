
def play_game(board):
    '''
	This function is used for starting tic tac toe game.

	Attributes :
		board = it takes the empty board for playing a game.
		
	'''
    print('Tap 1 for Multiplayer')
    print('Tap 2 for play with Computer')
    
    choice = input('Enter your choice: ')
    count = 0
    turn = 0

    if choice == '1':  # Multiplayer Mode
        print('\nSelect between these 2 characters X and O:')

        while True : 

            char1 = input('Player 1 choice: ')
            if char1.lower() == 'x':
                char2 = 'O'
                break
            elif char1.lower() == 'o':
                char2 = 'x'
                break
            else:
                print("Please enters 'x' or 'o'  only!")

        while count < 9:
            print(f'\nPlayer 1 ({char1})' if count % 2 == 0 else f'Player 2 ({char2})')
            current_char = char1 if count % 2 == 0 else char2
            make_move(board, current_char)
            count += 1

            if check_winner(board, current_char):
                print(f'{("Player 2" if count % 2 == 0 else "Player 1")} won!')
                return

        print("It's a draw!")

    elif choice == '2':  # Play with Computer
        print('\nSelect between these 2 characters X and O:')
        while True : 
            char1 = input('Player 1 choice: ')
            if char1.lower() == 'x':
                computer  = 'O'
                break
            elif char1.lower() == 'o':
                computer = 'x'
                break
            else:
                print("Please enters 'x' or 'o'  only!")
        while turn < 9:
            print(f'Player ({char1})' if turn % 2 == 0 else 'Computer')
            current_char = char1 if turn % 2 == 0 else computer
            if turn % 2 == 0:
                make_move(board, current_char)
            else:
                computer_move(board, computer, char1)

            turn += 1
            if check_winner(board, current_char):
                print(f'{("Computer" if turn % 2 == 0 else "Player")} won!')
                return

        print("It's a draw!")

    else:
        print('Invalid choice, please try again.')
        play_game(board)


def show_board(board):
    '''
	This function is used for showing the board with the filled elements

    Attributes :
		board = it show the board after updation.
	
	'''    
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def make_move(board, ch):
    '''
	This function is used for inserting a element into the board if the position are empty

	Attributes :
		board = it has a element that are present in the board
		ch = it has a character that are sent in the argument by player
	'''
    while True:
        position = input(f'Enter the position (1-9) where you want to place {ch}: ')
        pos_map = {
            '1': (0, 0), '2': (0, 1), '3': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '7': (2, 0), '8': (2, 1), '9': (2, 2)
        }

        if position in pos_map:
            row, col = pos_map[position]
            if board[row][col] == ' ':
                board[row][col] = ch
                show_board(board)
                break
            else:
                print('This position is already taken. Try again.')
        else:
            print('Invalid position. Choose a number between 1 and 9.')


def check_winner(board, player):

    '''
	This function is used for checking which player wins the game.

	Attributes : 
		board = it has elements that are present in the board
		player = it has character for checking the winner 

	'''

    row = col = 3
    # Check rows, columns, and diagonals
    for i in range(row):
        if all([board[i][j] == player for j in range(col)]) or all([board[j][i] == player for j in range(col)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def computer_move(board, computer, user_move):
    '''
	This function is used for Computer move in which it ensures that computer try to win it first and if not then try to make the game draw and return their move.

	Attributes :
		board = it has elements in the board
		computer = it has a computer character
		user_move = it has a user character
	'''    
    print("Computer's move:")
    best_move = find_best_move(board, computer, user_move)
    row, col = best_move
    board[row][col] = computer
    show_board(board)


def minimax(board, depth, is_maximizing, computer, user):

    """
    This function is used for checking all the possibilty for the computer for finding the best move

    Attributes :
        board : it has all the elements that are present in the board 
        depth : it is like a instance for finding a best move
        is_maximizing : tell the system that this is computer or not 
        computer : it has a computer character 
        user : it has a player character.

    """

    row = col = 3

    if check_winner(board, computer):
        return 10 - depth
    
    if check_winner(board, user):
        return depth - 10
    
    if all(board[i][j] != ' ' for i in range(row) for j in range(col)):
        return 0

    if is_maximizing:
        max_score = float('-inf')
        for i in range(row):
            for j in range(col):
                if board[i][j] == ' ':
                    board[i][j] = computer
                    score = minimax(board, depth + 1, False, computer, user)
                    board[i][j] = ' '
                    max_score = max(max_score, score)
        return max_score

    else:
        min_score = float('inf')
        for i in range(row):
            for j in range(col):
                if board[i][j] == ' ':
                    board[i][j] = user
                    score = minimax(board, depth + 1, True, computer, user)
                    board[i][j] = ' '
                    min_score = min(min_score, score)
        return min_score


def find_best_move(board, computer, user):

    """
    This function is used for finding the best move for the computer 
    Attributes :

        board : it has all the elements that are present in the board
        computer : it contain computer character 
        user : it contain user character
    
    """
    row = col = 3
    best_move = None
    best_value = float('-inf')
    for i in range(row):
        for j in range(col):
            if board[i][j] == ' ':
                board[i][j] = computer
                move_value = minimax(board, 0, False, computer, user)
                board[i][j] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

if __name__ == '__main__':

    # Create an empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print('Welcome to Tic-Tac-Toe!\n')
    play_game(board)
