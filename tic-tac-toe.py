import random
# from IPython.display import clear_output
def display(board):
    print(board[7]+ '|'+ board[8]+'|'+ board[9])
    print(board[4]+ '|'+ board[5]+'|'+ board[6])
    print(board[1]+ '|'+ board[2]+'|'+ board[3])

def player_input():
    i = ''
    while not(i == 'X' or i == 'O'):
        i = input('Player X or O(in capitls): ')
    if i == 'X' or i == 'x':
        return ('X','O')
    else:
        return ('O','X')
def positioning(board, marker, position):
    board[position] = marker
def checking(board, mark):
    return((board[7]== mark and board[8]== mark and board[9]== mark)or
            (board[4]== mark and board[5]== mark and board[6]== mark)or
            (board[1]== mark and board[2]== mark and board[3]== mark)or
            (board[1]== mark and board[4]== mark and board[7]== mark)or
            (board[2]== mark and board[5]== mark and board[8]== mark)or
            (board[3]== mark and board[6]== mark and board[9]== mark)or
            (board[1]== mark and board[5]== mark and board[9]== mark)or
            (board[7]== mark and board[5]== mark and board[3]== mark))

def toss():
    toss_list = ['H', 'T']
    t = input("Player 1, Choose Heads(H) or Tails(T): ")
    f = random.choice(toss_list)
    if f == t:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_next_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9) : "))
    return position

def repeat():
    choice = input("Wanna Play again! Enter Yes or No")
    return choice == 'Yes'

print("!!!Welcome to Tic Tac Toe Game!!!")
board = [' ']*10
player1_marker, player2_marker = player_input()

turn = toss()
print(turn+' plays first')

play_game = input("Shall we start the game? y or n: ")
if play_game == 'y':
    start_game = True
else:
    start_game = False

while start_game:
    if turn == 'Player 1':
        display(board)
        position = player_next_choice(board)
        positioning(board,player1_marker, position)
        if checking(board,player1_marker):
            display(board)
            print("!!!PLAYER 1 HAS WON!!!")
            start_game = False
        else:
            if full_board_check(board):
                display(board)
                print("!!!TIE GAME!!!")
                start_game = False
            else:
                turn = 'Player 2'
    else:
        display(board)
        position = player_next_choice(board)
        positioning(board,player2_marker, position)
        if checking(board,player2_marker):
            display(board)
            print("!!!PLAYER 2 HAS WON!!!")
            start_game = False
        else:
            if full_board_check(board):
                display(board)
                print("!!!TIE GAME!!!")
                start_game = False
            else:
                turn = 'Player 1'
    if not repeat():
        break