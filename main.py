import numpy as np
import random


WINNING_SCORE = 4

# Check the win condition based on the last played column
def max_connecting(board):
    if np.all(board == 0):
        return 0

    # find any 4 squares that add to 4 or minus 4
    connect_length = WINNING_SCORE

    # Keep track of the max number of connecting disks
    max_connecting = 0

    # Check vertical
    for col in range(0, board.shape[1]):
        for rows in range(0, board.shape[0]-connect_length+1):
            checksum = np.sum(board[rows:rows+connect_length, col])
            if abs(checksum) > max_connecting:
                max_connecting = abs(checksum)

    # Check horizontal - must be at highest taken slot
    for col in range(0, board.shape[1]-connect_length+1):
        for row in range(0, board.shape[0]):
            checksum = np.sum(board[row,col:col+connect_length])
            if abs(checksum) > max_connecting:
                max_connecting = abs(checksum)

    # Check the 2 diagonals
    direcs = [ [1,1],
               [1,-1] ]

    for d in direcs:
        for start_x in range(0, board.shape[1]):
            for start_y in range(0, board.shape[0]):
                checksum = 0
                x = start_x
                y = start_y
                prev_val = board[y, x]
                while (y >= 0) & (y < board.shape[0]) & (x >= 0) & (x < board.shape[1]):
                    if (board[y, x] != 0) & (board[y, x] == prev_val):
                        checksum += 1
                        if checksum > max_connecting:
                            max_connecting = checksum
                    else:
                        checksum = 1

                    x += d[1]
                    y += d[0]

    return max_connecting


# Convert move order board to simpler 'colours' board
def orders_to_colours(board):
    # Turns are alternate so we can just find odd and even numbers
    colour_board = board % 2
    # Then subtract 1 from the zeroes to help with win condition checking
    colour_board[ colour_board ==0 ] = -1
    return colour_board

# Print the board
def print_board(board):
    print(board)

def make_move_AI(board):
    # If opponent could get win condition, block it
    # For each slot
    for x in range(0, board.shape[1]):
        for y in range(0, board.shape[0]):
            # That is currently empty
            if board[y, x] == 0:
                future_board = np.copy(board)
                # If the player takes it
                future_board[y, x] = 1
                # If that causes them to win
                if max_connecting(future_board) == WINNING_SCORE:
                    # Let's do that instead
                    return x

    # Otherwise, try to extend own placing
    # For each slot
    current_max = max_connecting(board)
    for x in range(0, board.shape[1]):
        for y in range(0, board.shape[0]):
            # That is currently empty
            if board[y, x] == 0:
                future_board = np.copy(board)
                # If the we take it
                future_board[y, x] = -1
                # If that causes them to win
                if max_connecting(future_board) == WINNING_SCORE:
                    # Let's do that instead
                    return x

    # Else, choose randomly
    return random.randint(0, board.shape[1]-1)


def make_move_AIv3(board):
    # Make even more optimal moves

    # If board is empty, take the middle
    if np.all(board == 0):
        return 3

    # If opponent could get win condition, block it
    # For each slot
    for x in range(0, board.shape[1]):
        for y in range(0, board.shape[0]):
            # That is currently empty
            if board[y, x] == 0:
                future_board = np.copy(board)
                # If the player takes it
                future_board[y, x] = 1
                # If that causes them to win
                if max_connecting(future_board) == WINNING_SCORE:
                    # Let's do that instead
                    return x

    # Otherwise, try to extend own placing
    # For each slot
    best_x = -1
    current_max = max_connecting(board)
    for x in range(0, board.shape[1]):
        for y in range(0, board.shape[0]):
            # That is currently empty
            if board[y, x] == 0:
                future_board = np.copy(board)
                # If we take it
                future_board[y, x] = -1
                new_max = max_connecting(future_board)
                # If that causes us to win
                if new_max == WINNING_SCORE:
                    # Let's do that
                    return x
                # Else if it increases the number we have in a row
                elif new_max > current_max:
                    best_x = x

    if best_x > -1:
        return best_x

    # Else, choose randomly
    return random.randint(0, board.shape[1]-1)


def make_move_AIv2(board):
    # Make more optimal moves

    # If board is empty, take the middle
    if np.all(board == 0):
        return 3

    # If opponent could get win condition, block it
    # For each slot
    for x in range(0, board.shape[1]):
        for y in range(0, board.shape[0]):
            # That is currently empty
            if board[y, x] == 0:
                future_board = np.copy(board)
                # If the player takes it
                future_board[y, x] = 1
                # If that causes them to win
                if max_connecting(future_board) == WINNING_SCORE:
                    # Let's do that instead
                    return x

    # Otherwise, try to extend own placing
    # For each slot
    current_max = max_connecting(board)
    for x in range(0, board.shape[1]):
        for y in range(0, board.shape[0]):
            # That is currently empty
            if board[y, x] == 0:
                future_board = np.copy(board)
                # If we take it
                future_board[y, x] = -1
                # If that causes us to win
                if max_connecting(future_board) == WINNING_SCORE:
                    # Let's do that!
                    return x

    # Else, choose randomly
    return random.randint(0, board.shape[1]-1)


def make_move_random(board):
    # Choose randomly
    return random.randint(0, board.shape[1]-1)


def make_move_human(board):
    # Human player, ask for input
    column_choice = -1
    while column_choice < 0 or column_choice > board.shape[0]:
        column_choice = int(input("Which column?"))
        # if column is already full, can't place here
        if board[0, column_choice] != 0:
            print("Invalid move, please choose again")
            column_choice = -1

    return column_choice


def play_connect_four(start_player, show=True):
    # Set up a board and initialise to zeros
    # Not that board dimensions are [y, x]
    board = np.zeros([6, 7], np.int)

    human_player = True

    if human_player:
        show = True

    if start_player == 0:
        active_player = -1
    else:
        active_player = 1

    turn_count = 0
    max_connect = 0
    while max_connect < WINNING_SCORE:
        if show:
            print_board(board)

        column_choice = -1
        if active_player == 1:
            column_choice = make_move_AIv3(board)
        else:
            if human_player:
                column_choice = make_move_human(board)
            else:
                column_choice = make_move_AIv2(board)

        # find the lowest empty slot
        old_turn_count = turn_count
        for y in range(board.shape[0]-1, -1, -1):
            if turn_count == old_turn_count:
                slot = board[y, column_choice]
                if board[y, column_choice] == 0:
                    board[y, column_choice] = active_player
                    active_player *= -1
                    turn_count += 1
            else:
                break

        max_connect = max_connecting(board)
        # If board is full
        if (np.all(board) != 0) & (max_connect < WINNING_SCORE):
            max_connect = 2*WINNING_SCORE

    active_player *= -1
    if active_player == 1:
        winner = "AI_new"
    elif active_player == -1:
        winner = "AI"

    if max_connect == 2*WINNING_SCORE:
        winner = "Draw"

    #if show:
    print_board(board)
    print("GAME OVER: " + winner)

    return winner


# Main gameloop
def main():
    num_games = 100
    AI_wins = 0
    random_wins = 0
    draws = 0
    for i in range(num_games):
        start_player = i%2
        winner = play_connect_four(start_player, False)
        if winner == "AI_new":
            AI_wins += 1
        elif winner == "AI":
            random_wins += 1
        else:
            draws += 1

    print(f"AI_new: {AI_wins} \nAI: {random_wins} \nDraws:: {draws}")

if __name__ == '__main__':
    main()

