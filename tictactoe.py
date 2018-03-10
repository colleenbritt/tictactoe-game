'''

Simple tic-tac-toe game.

'''

def print_board(board):
    print ("    |   |   ")
    print ("  " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print (" ___|___|___")
    print ("    |   |   ")
    print ("  " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print (" ___|___|___")
    print ("    |   |   ")
    print ("  " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print ("    |   |   \n")


def print_instructions():
    print ("Use the following to make your move:")
    print ("   Top-left: 1,    Top-center: 2, Top-right: 3")
    print ("Middle-left: 4,        Center: 5, Middle-right: 6")
    print ("Bottom-left: 7, Bottom-center: 8, Bottom-right: 9 \n")

def game_description():
    print ("\n********************************")
    print ("*    Two-player Tic-tac-toe    *")
    print ("********************************")
    print ()

def get_input(symbol):
    valid_move = False
    while not valid_move:
        try:
            move = input ("Pick a position to place \"" + symbol + "\":  ")
            move = int(move)
            if move >= 1 and move <= 9:
                return move - 1
            else:
                print ("Invalid move. Try again.\n")
                print_instructions()
        except Exception as e:
            print (move + " is an invalid move. Try again!\n")


def check_board(board):
    win_combos = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
    for combo in win_combos:
        if board[combo[0]-1] == board[combo[1]-1] and board[combo[1]-1] == board[combo[2]-1]:
            return board[combo[0]-1]
    return 0


def end_game(board, message):
    print_board(board)
    print(message)
    quit()


def main():
    game_description()
    board = [" "," "," "," "," "," "," "," "," "]
    win = False
    num_moves = 0
    player = 1

    while not win:
        print_board(board)
        print_instructions()
        print ("It's player " + str(player) + "'s turn!\n")
        if player == 1:
            symbol = "X"
        else:
            symbol = "O"

        player_input = get_input(symbol)
        while board[player_input] != " ":
            print ("Cell already taken. Please try again!")
            player_input = get_input(symbol)
        if player == 1:
            board[player_input] = "X"
            player = 2
        else:
            board[player_input] = "O"
            player = 1

        num_moves += 1
        if num_moves > 4:
            winner = check_board(board)
            if winner != 0 and winner != " ":
                if winner == "X":
                    message = "\nPlayer 1 is the winner!\n"
                else:
                    message = "\nPlayer 2 is the winner!\n"
                end_game(board, message)
            elif num_moves == 9:
                message = "No winner!"
                end_game(board, message)


if __name__ == "__main__":
    main()