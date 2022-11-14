# Usefull Libraries
import os
import random
import re

# Display the board 
def display_board(board):
    os.system('cls')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Taking input from the user
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Please Choose [X or O]:").upper()

    player1 = marker
    if player1 == 'X':
        return('X','O')
    else:
        return('O','X')
   
# To place value on board list
def place_marker(board, marker, position):
    board[position] = marker

# To check win
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# To select who goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return('Player2')
    else:
        return('Player1')

# TO CHECK FOR FREE SPACE ON THE BOARD
def space_check(board, position):
    return board[position] == ' '


# TO CHECK THE BOARD IS FULL
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i) == True:
            return(False)
    return(True)

# TO ASK THE PLACE TO ENTER ON THE BOARD
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or  not space_check(board, position):
        position = int(input("Choose a Position (1-9):"))
    return(position)

# TO ASK TO CONTINUE THE GAME
def replay():
    return(input('Do You want to continue [Y or N]?').upper().startswith('Y'))

# THE ACTUAL CODE TO WORK THIS GAME !!! LOGIC
print('Welcome to Tic Tac Toe!')
while True:
# Set the game up here
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn +' will go First.')
    play_game = input('Ready to play the game?[y or N]').upper()
    if play_game[0] == 'Y':
        game_on = True
    else:
        game_on = False
    # pass
    while game_on:
        # Player 1 Turn
        if turn == 'Player1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            # CHECK FOR THE WIN
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congratulations Player 1 won!!")
                game_on = False
            else:
                # Check for the TIE
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Its a Tie!")
                    break
                else:
                    turn = 'Player2'
        else:
            # Player2's turn.
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            # CHECK FOR THE WIN
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congratulations Player2  won!!")
                game_on = False
            else:
                # Check for the TIE
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Its a Tie!")
                    break
                else:
                    turn = 'Player1'        
    if not replay():
        break

