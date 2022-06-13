#this is an addition/change made to the basic game
#allowing the first player to decide which symbol to use
#this may change code/method significantly 

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
