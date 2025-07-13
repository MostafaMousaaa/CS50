import math
import random
from cs50 import get_string

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """Return starting state of the board"""
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """Return player who has the next turn"""
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    return X if x_count <= o_count else O

def actions(board):
    """Return set of all possible actions available on the board"""
    possible_actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions

def result(board, action):
    """Return the board that results from making move (i, j) on the board"""
    if action not in actions(board):
        raise Exception("Invalid action")
    
    i, j = action
    new_board = [row[:] for row in board]  # Deep copy
    new_board[i][j] = player(board)
    
    return new_board

def winner(board):
    """Return the winner of the game, if there is one"""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """Return True if game is over, False otherwise"""
    return winner(board) is not None or len(actions(board)) == 0

def utility(board):
    """Return 1 if X has won the game, -1 if O has won, 0 otherwise"""
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """Return the optimal action for the current player on the board"""
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # Maximizing player
        _, action = max_value(board)
        return action
    else:
        # Minimizing player
        _, action = min_value(board)
        return action

def max_value(board):
    """Return maximum value and corresponding action"""
    if terminal(board):
        return utility(board), None
    
    v = -math.inf
    best_action = None
    
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    
    return v, best_action

def min_value(board):
    """Return minimum value and corresponding action"""
    if terminal(board):
        return utility(board), None
    
    v = math.inf
    best_action = None
    
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    
    return v, best_action

def minimax_alpha_beta(board, alpha=-math.inf, beta=math.inf):
    """Minimax with alpha-beta pruning for efficiency"""
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        _, action = max_value_ab(board, alpha, beta)
        return action
    else:
        _, action = min_value_ab(board, alpha, beta)
        return action

def max_value_ab(board, alpha, beta):
    """Max value with alpha-beta pruning"""
    if terminal(board):
        return utility(board), None
    
    v = -math.inf
    best_action = None
    
    for action in actions(board):
        min_val, _ = min_value_ab(result(board, action), alpha, beta)
        if min_val > v:
            v = min_val
            best_action = action
        alpha = max(alpha, v)
        if beta <= alpha:
            break  # Beta cutoff
    
    return v, best_action

def min_value_ab(board, alpha, beta):
    """Min value with alpha-beta pruning"""
    if terminal(board):
        return utility(board), None
    
    v = math.inf
    best_action = None
    
    for action in actions(board):
        max_val, _ = max_value_ab(result(board, action), alpha, beta)
        if max_val < v:
            v = max_val
            best_action = action
        beta = min(beta, v)
        if beta <= alpha:
            break  # Alpha cutoff
    
    return v, best_action

def print_board(board):
    """Print the board in a nice format"""
    print("   0   1   2")
    for i in range(3):
        print(f"{i}  ", end="")
        for j in range(3):
            cell = board[i][j] if board[i][j] is not None else " "
            print(f"{cell}", end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("   ---------")

def get_human_move(board):
    """Get move from human player"""
    while True:
        try:
            move_str = get_string("Enter your move (row col): ")
            row, col = map(int, move_str.split())
            
            if (row, col) in actions(board):
                return (row, col)
            else:
                print("Invalid move! Cell is already occupied.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column (0-2).")

def play_game():
    """Play a complete game of tic-tac-toe"""
    board = initial_state()
    human = None
    ai = None
    
    # Choose who goes first
    while True:
        choice = get_string("Play as X or O? (X goes first): ").upper()
        if choice in [X, O]:
            human = choice
            ai = O if human == X else X
            break
        print("Please choose X or O")
    
    print(f"\nYou are {human}, AI is {ai}")
    print("Enter moves as 'row col' (e.g., '1 2' for center-right)")
    
    while not terminal(board):
        print("\nCurrent board:")
        print_board(board)
        
        current_player = player(board)
        
        if current_player == human:
            print(f"\nYour turn ({human}):")
            move = get_human_move(board)
        else:
            print(f"\nAI's turn ({ai}):")
            print("AI is thinking...")
            move = minimax_alpha_beta(board)
            print(f"AI chooses: {move[0]} {move[1]}")
        
        board = result(board, move)
    
    print("\nFinal board:")
    print_board(board)
    
    winner_player = winner(board)
    if winner_player:
        if winner_player == human:
            print("Congratulations! You won!")
        else:
            print("AI won! Better luck next time.")
    else:
        print("It's a tie!")

def demonstrate_minimax():
    """Demonstrate minimax algorithm step by step"""
    print("=== Minimax Algorithm Demonstration ===")
    
    # Create a near-end game state
    demo_board = [
        [X, O, X],
        [O, X, EMPTY],
        [EMPTY, EMPTY, O]
    ]
    
    print("Demo board state:")
    print_board(demo_board)
    
    current_player = player(demo_board)
    print(f"\nCurrent player: {current_player}")
    print(f"Available actions: {actions(demo_board)}")
    
    # Show minimax decision
    best_move = minimax(demo_board)
    print(f"Minimax recommends: {best_move}")
    
    # Show what happens with each possible move
    print("\nAnalyzing each possible move:")
    for action in actions(demo_board):
        new_board = result(demo_board, action)
        game_over = terminal(new_board)
        if game_over:
            win = winner(new_board)
            if win:
                print(f"Move {action}: {win} wins!")
            else:
                print(f"Move {action}: Tie game")
        else:
            print(f"Move {action}: Game continues")

def main():
    """Main program"""
    print("=== Tic-Tac-Toe with Minimax AI ===")
    
    while True:
        print("\nOptions:")
        print("1. Play against AI")
        print("2. Watch AI vs AI")
        print("3. Demonstrate Minimax")
        print("4. Exit")
        
        choice = get_string("Choose an option: ")
        
        if choice == "1":
            play_game()
        elif choice == "2":
            print("AI vs AI game:")
            board = initial_state()
            move_count = 0
            
            while not terminal(board):
                print(f"\nMove {move_count + 1}:")
                print_board(board)
                current = player(board)
                move = minimax_alpha_beta(board)
                print(f"{current} plays: {move[0]} {move[1]}")
                board = result(board, move)
                move_count += 1
                
                if move_count > 9:  # Safety check
                    break
            
            print("\nFinal board:")
            print_board(board)
            winner_player = winner(board)
            if winner_player:
                print(f"{winner_player} wins!")
            else:
                print("Tie game!")
                
        elif choice == "3":
            demonstrate_minimax()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
