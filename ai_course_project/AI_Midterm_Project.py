board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
PLAYER_X = 'x'
AI_O = 'o'

def print_board(board):
    print("\nTic-Tac-Toe Board:")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def get_player_move(board):
    while True:
        try:
            move = input(f"Your turn ({PLAYER_X}). Select a position (1-9): ")
            move_index = int(move) - 1

            if 0 <= move_index <= 8:
                if board[move_index] == move:
                    return move_index
                else:
                    print("This position is choosen please choose an empty spot.")
            else:
                print("Invalid move please enter a number between 1-9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_game_state(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c]:
            return board[a]

    for spot in board:
        if spot.isdigit():
            return None
            
    return 'draw'

scores = {
    AI_O: 10,
    PLAYER_X: -10,
    'draw': 0
}

def get_empty_spots(board):
    spots = []
    for i, spot in enumerate(board):
        if spot.isdigit():
            spots.append(i)
    return spots

def minimax(current_board, is_maximizing_player):
    state = check_game_state(current_board)
    if state is not None:
        return scores.get(state, 0)

    if is_maximizing_player:
        best_score = -float('inf')
        for move_index in get_empty_spots(current_board):
            original_spot = current_board[move_index]
            current_board[move_index] = AI_O
            
            score = minimax(current_board, False)
            
            current_board[move_index] = original_spot
            best_score = max(score, best_score)
        return best_score
    
    else:
        best_score = float('inf')
        for move_index in get_empty_spots(current_board):
            original_spot = current_board[move_index]
            current_board[move_index] = PLAYER_X
            
            score = minimax(current_board, True)
            
            current_board[move_index] = original_spot
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move_index = -1
    
    for move_index in get_empty_spots(board):
        original_spot = board[move_index]
        board[move_index] = AI_O
        
        move_score = minimax(board, False)
        
        board[move_index] = original_spot
        
        if move_score > best_score:
            best_score = move_score
            best_move_index = move_index
            
    return best_move_index

def main_game_loop():
    current_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = PLAYER_X

    while True:
        print_board(current_board)

        if current_player == PLAYER_X:
            move_index = get_player_move(current_board)
            current_board[move_index] = PLAYER_X
            current_player = AI_O
        else:
            print(f"AI ({AI_O}) is thinking...")
            move_index = find_best_move(current_board)
            current_board[move_index] = AI_O
            current_player = PLAYER_X

        game_result = check_game_state(current_board)
        if game_result is not None:
            print_board(current_board)
            if game_result == 'draw':
                print("the game is a draw")
            else:
                print(f"player '{game_result}' won")
            break

main_game_loop()