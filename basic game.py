#global variables
board_spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
empty_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#creating a playboard w/print statements
def playboard():
    print('  |   |   ')
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('  |   |   ')
    print('---------') 
    print('  |   |   ')
    print(board[6]+' | '+board[7]+' | '+board[8])
    print('  |   |   ')
    
#player symbols and marked spaces
def player_inputs(player):
    player_sym = ['X', 'O']
    free_space = True
    pos = int(input('Player {playerNo} turn! Choose a space!'.format(playerNo = player +1)))

    if board[pos] == 'X' or board[pos] == 'O':
        free_space = False
        
    if not free_space:
        print('Space taken!')
        player_inputs(player)
    else:
        empty.remove(pos)
        board[pos] = player_sym[player]
        return 1
    
#winner winner chicken dinner
#def symbols, winning pos, and check for win
def wwcd():
    player_sym = ['X', 'O']
    winning_pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #rows, columns, diagonals
    for check in winning_pos:
        first_symbol = board[check[0]]
        if first_symbol != ' ':
            won = True
            for point in check:
                if playboard[point] !=  first_symbol:
                    won = False
                break
            if won:
                if first_sym == player_sym[0]:
                    print('player 1 won')
                else:
                    print('player 2 won')
                break
        else:
            won = False
    if won:
        return 0
    else:
        return 1
    
#gametime!
def gametime():
    player = 0
    while empty_spaces and wwcd():    
        playboard()
        player_inputs(player)
        player = int(not player)
    if not empty_spaces:
        print("NO WINNER!")
        
gametime()

#This is not done
#issues in wwcd with iterable objects
#i have rushed into this a bit too quickly theres a whole bunch of mistakes w/num, spelling, var names, etc
#and not enough bleeding comments
