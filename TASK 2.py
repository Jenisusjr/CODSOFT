import math

# Initialize board
board = [" " for _ in range(9)]  # 3x3 board stored in a list

def print_board():
    """Prints the Tic-Tac-Toe board"""
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def is_winner(player):
    """Checks if a player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def is_draw():
    """Checks if the game is a draw"""
    return " " not in board

def minimax(is_maximizing):
    """Minimax algorithm to find the best move for AI"""
    if is_winner("O"):  # AI wins
        return 1
    if is_winner("X"):  # Human wins
        return -1
    if is_draw():  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def best_move():
    """Finds the best move for the AI using Minimax"""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play():
    """Main game loop"""
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    for turn in range(9):
        if turn % 2 == 0:  # Human's turn
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if board[move] == " ":
                        board[move] = "X"
                        break
                    else:
                        print("Cell already occupied! Choose another.")
                except (ValueError, IndexError):
                    print("Invalid input! Enter a number between 1-9.")
        else:  # AI's turn
            move = best_move()
            board[move] = "O"
            print("\nAI chooses:", move + 1)

        print_board()

        if is_winner("X"):
            print("Congratulations! You win! 🎉")
            return
        if is_winner("O"):
            print("AI wins! Better luck next time. 🤖")
            return
        if is_draw():
            print("It's a draw! 😐")
            return

# Start the game
play()