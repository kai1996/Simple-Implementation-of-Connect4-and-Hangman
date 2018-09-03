""" 
Invalid moves is checked in both player1_move and player2_move functions 
after the move is made
Checks the tie
Checks for 4 in a row
Check for both types of diagonal wins

If you want to see the actual working within the lists I have added them in the code 
but uncommented it in the player move function
"""


#CONSTANTS
BOARD_COLUMNS=7
BOARD_ROWS=6




def lists_within_lists():
    
    """
    This function creates a list within a list. The outer list has indices that refer 
    to the columns and the inner lists refer to rows within the columns. This function 
    works on any size of the board column and board rows
    """
    
    lists1=[] #Creates an empty outer list
    
    for i in range(BOARD_COLUMNS):#loops through the outer list
        lists1.append([])
        
        for j in range(BOARD_ROWS):#loops through the inner list
            lists1[-1].append('')
            #Adds an empty value to each elements in the inner lists.This is used 
            #in the program to refer to values and change values in the game
            
    return lists1
 
 
 
 
 
def player1_move(lists):
    """
    This function governs the move of player one i.e. "x". It will also check for invalid 
    move that will be more than the number of rows. It loops through the board rows and 
    checks if the space chosen by the user is empty. If it is, it replaces the emptiness
    with "x". 
    """
    move=int(input("enter a number between 1 to 7: "))
    move=move-1
    #Prompts the player 1 to decide his move in the board space that is referred 
    #by numbers from 0 to the number of rows. 
    
    if move>BOARD_ROWS:               #To check invalid move 
       print("Invalid move")
       player1_move(lists)
    elif move<0:               #To check invalid move 
       print("Invalid move")
       player1_move(lists)
    else:
        for i in range(BOARD_ROWS):        
            if lists[move][i]=='':
                lists[move][i]='x'   #Replaces the empty value with "x"
#                print(lists)
                break                #Ends the loop as the objective is met
    return(lists)
    
    





def player2_move(lists):

    """
    This function governs the move of player two i.e. "o". It will also check for invalid 
    move that will be more than the number of rows. It loops through the board rows and 
    checks if the space chosen by the user is empty. If it is, it replaces the emptiness
    with "o". This function is created so that the code looks clean and more understandable
    """
    move=int(input("enter a number between 0 to 6: "))
    move=move-1
    if move>BOARD_ROWS:
       print("Invalid move") #Checks for invalid move
       player2_move(lists)
    elif move<0:               #To check invalid move 
       print("Invalid move")
       player2_move(lists)
    else:
        for i in range(BOARD_ROWS):        
            if lists[move][i]=='':
                lists[move][i]='o'
#                print(lists)
                break
    return(lists)
    
    
    
    
    
    
    
    
    

def play_connect4():
    
    """
    This function runs the actual game of Connect 4. Basically, two players 
    play a move alternately and the first to get 4 of their move(either "x" or "o")
    in a row(horizontally, vertically, or diagonally) wins the game. This function also 
    check if a valid move is made. It imports the functions that draw a visual representation
    of the board and check the winner based on horizontal, vertical, or diagonal wins. Those 
    functions are defined in the program. 
    """
    
    moves=0 #THe number of total moves made is started with 0.
    lists = lists_within_lists()
    visual_board(lists)#imports the visual board
    
    while moves<(BOARD_ROWS*BOARD_COLUMNS):
        #BOARD_ROWS*BOARD_COLUMNS gives the total possibilities in the board to be played.
        #Once, it is achieved, the computer can understand the board is full
        
        
            player1_move(lists)
            #Calls the player1_move function that allows for movement for player 1.  
            visual_board(lists)
            #prints the visual board with the appended move
            moves+=1
            #increments the move so that we keep check if the board is full
            check_winner_vertical(lists)
            if check_winner_vertical(lists)==True:
               break  #Breaks the code so once this occurs the game is over
           
            check_winner_horizontal(lists)
            if check_winner_horizontal(lists)==True:
               break
           
            check_winner_diagonal_positive_player(lists)
            check_winner_diagonal_negative_player(lists)
            if check_winner_diagonal_positive_player(lists)==True or check_winner_diagonal_negative_player(lists)==True:
               break
            
            
            player2_move(lists)  
            visual_board(lists)
            moves+=1
            
            if check_winner_vertical(lists)==False:
               break
           
            check_winner_horizontal(lists)
            if check_winner_horizontal(lists)==False:
               break
           
            check_winner_diagonal_positive_player(lists)
            check_winner_diagonal_negative_player(lists)
            if check_winner_diagonal_positive_player(lists)==False or check_winner_diagonal_negative_player(lists)==False:
               break
    return
    print("It's a tie") 
    play_again=input("Do you want to play again(y/n)? " )
    if play_again.lower()=="y":
        play_connect4(lists)# calls the function again so that game can be played 
#    print(lists)
    






def check_winner_vertical(lists):
    """
    This function checks the winner based on a vertical win in the board matrix. It will take a value 
    in the board as a reference and checks if there are 3 more of the same values in a vertical order
    in a consecutive manner. If there is, it is a vertical win. It then passes the information 
    as a boolean expression True if player 1 wins and False if Player 2 wins. 
    """
    for i in range(BOARD_COLUMNS):
        for j in range(BOARD_ROWS-4):
            if lists[i][j]=="x" and lists[i][j+1]=="x" and lists[i][j+2]=="x" and lists[i][j+3]=="x":
               print("Player 1 wins") 
               return True
            elif lists[i][j]=="o" and lists[i][j+1]=="o" and lists[i][j+2]=="o" and lists[i][j+3]=="o":
                print("Player 2 wins")                
                return False
 
 
 
 
 
 
def check_winner_horizontal(lists):  
   
    """
    This function checks the winner based on a horizontal win in the board matrix. It will take a value 
    in the board as a reference and checks if there are 3 more of the same values in a horizontal order
    i.e. along the column in a consecutive manner. If there is, it is a horizontal win. It then passes the information 
    as a boolean expression True if player 1 wins and False if Player 2 wins. 
    """
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLUMNS-4):
            if lists[i][j]=="x" and lists[i+1][j]=="x" and lists[i+2][j]=="x" and lists[i+3][j]=="x":
               print("Player 1 wins") 
               return True
            elif lists[i][j]=="o" and lists[i+1][j]=="o" and lists[i+2][j]=="o" and lists[i+3][j]=="o":
               print("Player 2 wins") 
               return False
               
               
               
               
               
def check_winner_diagonal_positive_player(lists):
    """
    This function checks the winner based on a diagonal win in the board matrix where the diagonal sloped in a positive direction.
    It will take a value in the board as a reference and checks if there are 3 more of the same value when both the values of rows and 
    columns are incremented by one. in a consecutive manner. If there is, it is a positive diagonal win. It then passes the information 
    as a boolean expression True if player 1 wins and False if Player 2 wins. 
    """
    for i in range(BOARD_COLUMNS-4):
        for j in range(BOARD_ROWS-4):
            if lists[i][j]=="x" and lists[i+1][j+1]=="x" and lists[i+2][j+2]=="x" and lists[i+3][j+3]=="x": 
                print("Player 1 wins")
                return True
            elif lists[i][j]=="o" and lists[i+1][j+1]=="o" and lists[i+2][j+2]=="o" and lists[i+3][j+3]=="o":
                print("Player 2 wins")                
                return False
                
                
                
                
                
def check_winner_diagonal_negative_player(lists):
    """
    This function checks the winner based on a diagonal win in the board matrix where the diagonal sloped in a negative direction.
    It will take a value in the board as a reference and checks if there are 3 more of the same value when one looks down one row and right one more column. in a consecutive manner. If there is, it is a negative diagonal win. 
    It then passes the information as a boolean expression True if player 1 wins and False if Player 2 wins. 
    """
    
    for i in range(BOARD_COLUMNS-4):
        for j in range(BOARD_ROWS-4):
            if lists[i][j+3]=="x" and lists[i+1][j+2]=="x" and lists[i+2][j+1]=="x" and lists[i+3][j]=="x": 
                print("Player 1 wins")
                return True
            elif lists[i][j+3]=="o" and lists[i+1][j+2]=="o" and lists[i+2][j+1]=="o" and lists[i+3][j]=="o":
                print("Player 2 wins")
                return False






def visual_board(lists):
    """
    This function creates a visual representation of the board created by the 
    lists_within_lists() function. It does so by assigning each values in each row of the list 
    and then prints those together in a way that every time the values are replaced, it 
    is observed in the board.  
    """
   
    j=''
    for l in range(1,BOARD_COLUMNS+1):
        #This is for the last line in the visual representation of the board that
        #the user uses as a reference to make the moves 
        j=j+"  "+ str(l)
        shortened= []
        
    for i in range(BOARD_ROWS-1,-1,-1):#Board_ROWS-1 because it decreases to 0 but the number of times as the board_rows
        
        for k in range(BOARD_COLUMNS):
            shortened.append(lists[k][i])#This appends the value assigned from the lists of lists function 
        print("|"+ " "+shortened[0]+"  "+shortened[1]+"  "+shortened[2]+"  "+shortened[3]+"  "+shortened[4]+"  "+shortened[5]+"  "+shortened[6]+"  "+ "      |")
        #This puts all the values of the row together        
        shortened = []
    final=print("+---------------------+"+"\n"+j)    
    return final
        
        
        
        
        
        
    
def main():
   """
   This is the main function that calls the function that plays the connect 4 game 
   """
   play_connect4()
   return
    







if __name__ == "__main__":
#TO check if the module was imported and the program runs when it is run
     play_connect4()
else:
    print("It is an imported Module")
