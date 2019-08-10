######################################
# THIS IS A CONNECT 4 GAME MADE WITH
# PYTHON IN PYCHARM
# PLAYERS INTERACT WITH THE GAME 
# USING A COMMAND LINE PROMPT
######################################
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

# CREATE THE CONNECT 4 BOARD

def create_board():
    return np.zeros((6, 7), dtype=int)


the_board = create_board()


# TO CHECK IF A COLUMN IS FULL

def is_valid(col):
    return the_board[0][col] == 0


# FIND THE NEXT FREE ROW IN THE SELECTED COLUMN

def next_open_row(col):
    for r in range(0, ROW_COUNT):
        if the_board[r][col] != 0:
            r = r-1
            break

    return r


# FUNCTION TO DROP THE PIECE INTO THE NEXT OPEN ROW

def drop_piece(current_row, col, piece):
    the_board[current_row][col] = piece


# IF THERE IS NO 0'S IN THE TOP ROW THE GAME IS A DRAW

def draw():
    if the_board[0][0] != 0 and the_board[0][1] != 0 and the_board[0][2] != 0 and the_board[0][3] != 0 and the_board[0][4] != 0 and the_board[0][5] != 0 and the_board[0][6] != 0:
        print('The Game Is A Draw')
        return True
    else:
        return False


# ASK THE PLAYERS IF THEY WANT TO PLAY AGAIN

def replay():
    ans = input('Do you want to play again? y or n: ')
    if ans[0].lower() == 'y':
        print('Thank you for playing')
        return True
    else:
        print('Thank you for playing')
        return False


# FUNCTION TO CHECK IF A PLAYER HAS 4 IN A ROW HORIZONTALLY

def horizontal_win_check(player):
    for row_num in range(0, ROW_COUNT):
        counter = 0
        for item in range(0, COLUMN_COUNT-1):
            if the_board[row_num][item] != 0:
                if the_board[row_num][item] == player and the_board[row_num][item] == the_board[row_num][item + 1]:
                    counter += 1
                else:
                    counter = 0

            if counter == 3:
                return True

            if item == COLUMN_COUNT-1:
                return False


# TO CHECK IF A PLAYER HAS 4 IN A ROW VERTICALLY

def vertical_win_check(player):
    for col_num in range(0, COLUMN_COUNT):
        counter = 0
        for item in range(0, ROW_COUNT-1):
            if the_board[item][col_num] != 0:
                if the_board[item][col_num] == player and the_board[item][col_num] == the_board[item+1][col_num]:
                    counter += 1
                else:
                    counter = 0

            if counter == 3:
                return True
            if item == ROW_COUNT - 1:
                return False


# TO CHECK IF A PLAYER HAS 4 IN A ROW DIAGONALLY

def diagonal_win_check(player):
    # POSITIVELY SLOPED DIAGONALS

    for col_num in range(COLUMN_COUNT - 3):

        for row_num in range(3, ROW_COUNT):

            if the_board[row_num][col_num] == player \
                    and the_board[row_num - 1][col_num + 1] == player \
                    and the_board[row_num - 2][col_num + 2] == player \
                    and the_board[row_num - 3][col_num + 3] == player:
                return True

    # NEGATIVE SLOPED DIAGONALS

    for col_num in range(COLUMN_COUNT - 3):

        for row_num in range(ROW_COUNT - 3):

            if the_board[row_num][col_num] == player \
                    and the_board[row_num + 1][col_num + 1] == player \
                    and the_board[row_num + 2][col_num + 2] == player \
                    and the_board[row_num + 3][col_num + 3] == player:
                return True


# FUNCTION THAT COMPILES ALL WAYS OF WINNING

def win_check():
    for player in range(1, 3):
        if horizontal_win_check(player):
            return print_and_return_win_status(player)
        elif vertical_win_check(player):
            return print_and_return_win_status(player)
        elif diagonal_win_check(player):
            return print_and_return_win_status(player)


def print_and_return_win_status(player):
    print('Player {} has won!'.format(str(player)))
    return True


# START THE GAME AND SET THE TURN TO BE PLAYER 1'S TURN

game_over = False
turn = 0
while not game_over:

    # ask player 1 for input
    if turn == 0:

        column = int(input('Player 1 choose where you want to go (0-6): '))
        if is_valid(column):
            row = next_open_row(column)
            drop_piece(row, column, 1)
            if win_check():
                print(the_board)
                if not replay():
                    game_over = True
                else:
                    the_board = create_board()
                    turn = 1
            if draw():
                print(the_board)
                if not replay():
                    game_over = True
                else:
                    the_board = create_board()
                    turn = 1

        else:
            print('This column is full try again')
            continue
    else:
        # player 2 selection
        column = int(input('Player 2 choose where you want to go (0-6): '))
        if is_valid(column):
            row = next_open_row(column)
            drop_piece(row, column, 2)
            if win_check():
                print(the_board)
                if not replay():
                    game_over = True
                else:
                    the_board = create_board()
                    turn = 1
            if draw():
                print(the_board)
                if not replay():
                    game_over = True
                else:
                    the_board = create_board()
                    turn = 1
        else:
            print('This column is full try again')
            continue


# AFTER EACH GO PRINT THE BOARD AND SET THE TURN TO THE OTHER PLAYER

    print(the_board)
    turn += 1
    turn = turn % 2
