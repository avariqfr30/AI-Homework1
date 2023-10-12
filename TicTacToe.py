import random

# Initialize the Tic-Tac-Toe board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Get a list of empty cells on the board
def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

# Player's move
def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if (0 <= row < 3) and (0 <= col < 3) and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers (0, 1, or 2) for row and column.")

# Computer's move using Minimax algorithm
def computer_move(board):
    if is_board_full(board):
        return None

    best_score = float("-inf")
    best_move = None

    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, False)
        board[row][col] = " "

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

# Minimax algorithm
def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score = minimax(board, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score = minimax(board, True)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score

# Main game loop
def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_row, player_col = player_move(board)
        board[player_row][player_col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win! Congratulations!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn:")
        computer_row, computer_col = computer_move(board)
        board[computer_row][computer_col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()