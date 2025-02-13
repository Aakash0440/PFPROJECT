import random

# Constants
HIDDEN_BLANK = 0
HIDDEN_MINE = -1
REVEALED_BLANK = 1
REVEALED_MINE = -2

# Function to clear the screen
def clear_screen():
    print("", end="")

# Function to create the game board
def create_board(width, height, num_mines):
    board = [[HIDDEN_BLANK for _ in range(width)] for _ in range(height)]
    
    # Place mines randomly
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, height - 1)
        col = random.randint(0, width - 1)
        if board[row][col] != HIDDEN_MINE:
            board[row][col] = HIDDEN_MINE
            mines_placed += 1
            
    return board

# Function to print the board
def print_board(board, revealed):
    width = len(board[0])
    height = len(board)
    
    print("   " + " ".join([str(i+1) for i in range(width)]))
    for row in range(height):
        row_str = [str(board[row][col]) if revealed[row][col] else "?" for col in range(width)]
        print(str(row+1) + "  " + " ".join(row_str))

# Function to reveal a cell
def reveal_cell(board, revealed, row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return
    if revealed[row][col]:
        return
    
    revealed[row][col] = True
    if board[row][col] == HIDDEN_MINE:
        return

    if board[row][col] == HIDDEN_BLANK:
        # Reveal surrounding cells if the current cell is a blank
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                reveal_cell(board, revealed, r, c)

# Function to check for win condition
def check_win(board, revealed):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != HIDDEN_MINE and not revealed[row][col]:
                return False
    return True

# Main function to play the game
def play_game():
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    num_mines = int(input("Enter the number of mines: "))
    
    board = create_board(width, height, num_mines)
    revealed = [[False for _ in range(width)] for _ in range(height)]
    
    while True:
        clear_screen()
        print_board(board, revealed)
        
        if check_win(board, revealed):
            print("Congratulations! You have won!")
            break
        
        row = int(input("Enter row number (1 to {}): ".format(height))) - 1
        col = int(input("Enter column number (1 to {}): ".format(width))) - 1
        
        if board[row][col] == HIDDEN_MINE:
            clear_screen()
            for r in range(height):
                for c in range(width):
                    revealed[r][c] = True
            print_board(board, revealed)
            print("Game Over! You hit a mine.")
            break
        
        reveal_cell(board, revealed, row, col)

play_game()
