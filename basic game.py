#global variables
board_spaces = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
empty_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#creating a playboard w/print statements
def playboard():
    print(board_spaces[1]+' | '+board_spaces[2]+' | '+board_spaces[3])
    print('---------')
    print(board_spaces[4]+' | '+board_spaces[5]+' | '+board_spaces[6])
    print('---------') 
    print(board_spaces[7]+' | '+board_spaces[8]+' | '+board_spaces[9]) 
    
#player symbols and marked spaces
def player_inputs(player):
    player_sym = ['X', 'O']
    free_space = True
    pos = int(input('Player {playerNo} turn! Choose a space!'.format(playerNo = player +1)))
    if board_spaces[pos] == 'X' or board_spaces[pos] == 'O':
        free_space = False
    if not free_space:
        print('Space taken!')
        player_inputs(player)
    else:
        empty_spaces.remove(pos)
        board_spaces[pos] = player_sym[player]
        return 1
    
#winner winner chicken dinner
#def symbols, winning pos, and check for win
#Rows,Columns,Diagonals
def wwcd():
  player_sym = ['X', 'O']
  winning_pos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
  for check in winning_pos:
    first_symbol = board_spaces[check[0]]
    if first_symbol != ' ':
      won = True
      for point in check:
        if playboard[point] !=  first_symbol:
          won = False
          break  
      if won:
        if first_symbol == player_sym[0]:
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
##10/6/22 - fixed point 2 but raised a tabbing issue
