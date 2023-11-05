import random
count =0
def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    player_turn = True  # True for player 1, False for AI

    while True:
        if player_turn:
            player_move(board, symbol_1)
        else:
            ai_move(board, symbol_2, symbol_1)

        pretty = printPretty(board)
        winner = isWinner(board, symbol_1, symbol_2)
        if winner == symbol_1:
            print("Player 1 wins!")
            break
        elif winner == symbol_2:
            print("AI wins!")
            break
        elif isBoardFull(board):
            print("It's a tie!")
            break

        player_turn = not player_turn

def intro():
    print("Hello! Welcome to Pam's Tic Tac Toe game against AI!")
    print("\n")
    print("Rules: You are player 1 (X), and you are playing against the AI (O). "
          "Take turns marking the spaces in a 3x3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")

def create_grid():
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def sym():
    symbol_1 = "X"
    symbol_2 = "O"
    print("You are X. AI is O.")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)

def player_move(board, symbol_1):
    while True:
        row = int(input("Pick a row (0, 1, or 2): "))
        column = int(input("Pick a column (0, 1, or 2): "))
        if is_valid_move(board, row, column):
            board[row][column] = symbol_1
            break
        else:
            print("Invalid move. Try again.")

def is_valid_move(board, row, column):
    return 0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == " "

def ai_move(board, symbol_2, symbol_1):
    move = 0
    best_score = -float("inf")
    best_move = None
    alpha = -float("inf")
    beta = float("inf")

    for row in range(3):
        for column in range(3):
            if board[row][column] == " ":
                board[row][column] = symbol_2
                score = minimax(board, 0, False, symbol_1, symbol_2, alpha, beta,move)
                board[row][column] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, column)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cutoff

    if best_move:
        board[best_move[0]][best_move[1]] = symbol_2
def minimax(board, depth, is_maximizing, symbol_1, symbol_2, alpha, beta,move):
    global count 
    count +=1
    scores = {"X": -1, "O": 1, "tie": 0}
    result = isWinner(board, symbol_1, symbol_2)
    if result:
        return scores[result]

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for column in range(3):
                if board[row][column] == " ":
                    board[row][column] = symbol_2
                    score = minimax(board, depth + 1, False, symbol_1, symbol_2, alpha, beta,move)
                    board[row][column] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break  # Beta cutoff
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for column in range(3):
                if board[row][column] == " ":
                    board[row][column] = symbol_1
                    score = minimax(board, depth + 1, True, symbol_1, symbol_2, alpha, beta,move)
                    board[row][column] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break  # Alpha cutoff
        return best_score

def isBoardFull(board):
    for row in board:
        if " " in row:
            return False
    return True

def printPretty(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def isWinner(board, symbol_1, symbol_2):
    for row in board:
        if row[0] == row[1] == row[2] == symbol_1:
            return symbol_1
        elif row[0] == row[1] == row[2] == symbol_2:
            return symbol_2

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol_1:
            return symbol_1
        elif board[0][col] == board[1][col] == board[2][col] == symbol_2:
            return symbol_2

    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        return symbol_1
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        return symbol_2

    if board[0][2] == board[1][1] == board[2][0] == symbol_1:
        return symbol_1
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        return symbol_2

    if isBoardFull(board):
        return "tie"

# Call Main
main()
print(count)