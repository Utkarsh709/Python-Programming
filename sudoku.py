import random

def create_puzzle(size):
    board = []
    num = "__"
    for i in range(size):
        row = []
        for j in range(size):
            row.append(num)
        board.append(row)
    
    for r in range(size):
        for c in range(size):
            n = random.randint(1, size)
            row_check = n not in board[r]
            col_check = n not in [rows[c] for rows in board]
            if row_check and col_check:
                board[r][c] = str(n)
            else:
                return create_puzzle(size)  
    
    return board 


def display(board):
    print("----" * len(board))
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("----" * len(board))


def initialize():
    size = int(input("Enter size: "))
    if size < 1:
        print("Size must be greater than 0.")
        return
    
    board = create_puzzle(size)  
    levels = {1: ("Very Easy", 20), 2: ("Easy", 30), 3: ("Medium", 50)}
    
    for k, v in levels.items():
        print(f"Level {k}: {v[0]}")
    
    level = int(input("Enter your difficulty level number: "))
    no_of_hidden_fields = (levels[level][1] * size * size) // 100
    original_board = [row.copy() for row in board]
    hidden_fields = []
    all_possibilities = list(range(size * size)) 
    for _ in range(no_of_hidden_fields):
        number = all_possibilities.pop(random.randint(0, len(all_possibilities) - 1))
        hidden_fields.append((number // size, number % size))
    
    for r_, c_ in hidden_fields:
        board[r_][c_] = "X"
    
    start_game(board, hidden_fields, original_board)


def start_game(board, hidden_fields, original_board):
    display(board)
    for rr_, cc_ in hidden_fields:
        board[rr_][cc_] = input(f"Enter value for row {rr_ + 1}, col {cc_ + 1}: ")
    
    stop_game(board, original_board)


def stop_game(board, original_board):
    is_correct = True
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != original_board[r][c]:
                is_correct = False
                print(f"Mismatch found at row {r + 1}, col {c + 1}")
    
    if is_correct:
        print("Congratulations! You solved the puzzle correctly!")
    else:
        print("Sorry, the puzzle has some mistakes. Please try again.")


def sudoku():
    initialize()


sudoku()

