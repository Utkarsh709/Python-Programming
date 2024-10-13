import random

def initialize_board():
    board = []
    num = 1
    for i in range(3):
        row = []
        for j in range(3):
            row.append(str(num))
            num += 1
        board.append(row)
    return board

def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def make_move(board, row, col, player):
    if board[row][col] not in ['X', 'O', 'A', 'B']:  
        board[row][col] = player
        return True
    else:
        return False

def tic_tac_toe():
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    player1_symbol = player1_name[0].upper()
    player2_symbol = player2_name[0].upper()
    current_player_name, current_player_symbol = random.choice([(player1_name, player1_symbol), (player2_name, player2_symbol)])
    print(f"{current_player_name} will play first with symbol '{current_player_symbol}'.")
    board = initialize_board()
    while True:
        print_board(board)
        print(f"{current_player_name}'s turn:")
        move = int(input("Enter a position (1-9): ")) - 1
        row, col = divmod(move, 3)
        if make_move(board, row, col, current_player_symbol): 
            if current_player_name == player1_name:
                current_player_name, current_player_symbol = player2_name, player2_symbol
            else:
                current_player_name, current_player_symbol = player1_name, player1_symbol
        else:
            print("Invalid move, try again.")

tic_tac_toe()

