#!/usr/bin/env python
# coding: utf-8

# *** TIC-TAC-TOE ***

# In[ ]:


from IPython.display import clear_output   #import function to clear previous output

#Function to display board
def display_board(test_board):
    print('\n')
    print('    | '+'    | ')
    print(' ' +test_board['7'] + '  | ' +' ' + test_board['8'] + '  | ' +' ' + test_board['9'] )
    print('    | '+'    | ')
    print('----------------' )
    print('    | '+'    | ')
    print(' ' +test_board['4'] + '  | ' +' ' + test_board['5'] + '  | ' +' ' + test_board['6'] )
    print('    | '+'    | ')
    print('----------------' )
    print('    | '+'    | ')
    print(' ' +test_board['1'] + '  | ' +' ' + test_board['2'] + '  | ' +' ' + test_board['3'] )
    print('    | '+'    | ')
    
    print('\n')

       
   
            
#Function to take input from player 1
def play1():
    while True:
        p1= str(input('Choose your position p1 (1-9)'))
        if p1 not in ['1','2','3','4','5','6','7','8','9']:
            print('Please choose 1-9 only')
        else:
            break
    return p1
    
#Function to take input from player 2
def play2():
    while True:
        p2= str(input('Choose your position p2 (1-9)'))
        if p2 not in ['1','2','3','4','5','6','7','8','9']:
            print('Please choose 1-9 only')
        else:
            break
    return p2
    
#Function to check winner
def check_winner(test_board):
    if(test_board['1'] ==  test_board['2'] == test_board['3']  and test_board['3']!= ' '  ) or (test_board['4'] ==  test_board['5'] == test_board['6']  and test_board['4']!= ' '  ) or(test_board['7'] ==  test_board['8'] == test_board['9']  and test_board['7']!= ' '  ) or(test_board['1'] ==  test_board['4'] == test_board['7']  and test_board['1']!= ' '  ) or(test_board['5'] ==  test_board['2'] == test_board['8']  and test_board['2']!= ' '  ) or(test_board['3'] ==  test_board['6'] == test_board['9']  and test_board['3']!= ' '  ) or(test_board['1'] ==  test_board['5'] == test_board['9']  and test_board['1']!= ' '  ) or(test_board['5'] ==  test_board['7'] == test_board['3']  and test_board['3']!= ' '  ) :
        return True

    else:
        return False 

#Function to replace user's input postion with X or O
def replace_map(play_board,test_board,player):
    clear_output()
    if test_board[play_board] == ' ':
        test_board[play_board] = player
        display_board(test_board)
        return True
    else:
        print('Please choose another position as postion {} is already taken by {}'.format(play_board,test_board[play_board]))
        display_board(test_board)
        return False
    

#Function to check if user wants to play again  
def play_again():
    play_again = str(input('Do you want to play again?'))
    if play_again.lower() == 'yes':
        return True
    else:
        return False

        
    

#Function to alternate players's turn and check winner after each turn
def play(player1,player2,test_board):
    count = 0
   
    while True:
        
        #print(winner)
        replaced = False
        while replaced == False : 
            play_board1 = play1()
            replaced = replace_map(play_board1,test_board,player1)
            
        else:
            winner = check_winner(test_board)
            count= count+1
            if winner == True:
                print('Player 1 wins')
                if play_again() == True:
                    user_input('yes')
                else: 
                    break
                #user_input()
            replaced = False
            while replaced == False : 
                play_board2 = play2()
                replaced = replace_map(play_board2,test_board,player2)
            else:
                winner2 = check_winner(test_board)
                count= count+1
                if winner2 == True:
                    print('Player 2 wins')
                    if play_again()== True:
                        user_input('yes')
                    else: 
                        break
                if count == 9 and winner!= True:
                    print('Its a Tie')
                    break
                    if play_again()== True:
                        user_input('yes')
                    else: 
                        break
        continue
                
            
#Function to take input from user        
def user_input(st):
    test_board = {'1' :' ','2' :' ','3' :' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    if st == ' ':
        result = str(input('Do you want to play Tic-Tac-Toe? Yes or No?'))
    else:
        result = st
    
    if result.lower() == 'yes':
        while True:
            player1 = str(input('Choose X or O player 1?'))  
            if player1.upper() not in ['X','O']:
                print('Please select X or O only')
                
            else:
                break
        if player1.upper() == 'X':
            player1 = 'X'
            player2 = 'O'
        else:
            player1 = 'O'
            player2 = 'X'
        print('player 2 is {}'.format(player2))
        display_board(test_board)
        play(player1,player2,test_board)
      
        

user_input(' ')


        

