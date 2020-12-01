#A TIC TAC TOE GAME FOR FUN
import random
#print('\033c')
board = ['#','X','O','X','O','X','O','X','O','X']
def displayBoard(board):
   
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
displayBoard(board)
'''
&&  and
==
!=
not 
or

list

'''


def playerInput():
    marker = ''
    sample = ['X','O']
    while not (marker == 'X' or marker == 'O'):
        marker = input("Enter your choice of marker\n").upper()
        if marker in sample:
            if(marker == 'X'):
                return ('X','O')
            else:
                return('O','X')
        else:
            print('\nChoose your marker again \nThe choice has to be either X or O')
#print(playerInput())


#Mark the position
def placeMarker(board,marker,position):
 
    board[position] = marker
    
#Check if any player has won 
def winCheck(board,marker):
    return( (board[1] == marker) and (board[2] == marker) and (board[3] == marker ) or
            (board[4] == marker) and (board[5] == marker) and (board[6] == marker ) or
            (board[7] == marker) and (board[8] == marker) and (board[9] == marker ) or

            (board[7] == marker) and (board[4] == marker) and (board[1] == marker ) or
            (board[8] == marker) and (board[5] == marker) and (board[2] == marker ) or
            (board[9] == marker) and (board[6] == marker) and (board[3] == marker ) or
           
            (board[7] == marker) and (board[5] == marker) and (board[3] == marker ) or
            (board[1] == marker) and (board[5] == marker) and (board[9] == marker )        
           )
#print(winCheck(board,'X'))


#Randomly choose a player
def chooseFirst():
    if(random.randint(1,2) == 1):
        return ('Player 1')
    else:
        return ('PLayer 2')
    
#print(chooseFirst())

#Function checks if there's empty space
def spaceCheck(board,position): 
    return board[position] == ' '

def fullBoardCheck(board):
    for pos in range(1,10):
        if spaceCheck(board,pos):
            return False
    else:
        return True
    
#Ask for players next position
def playerChoice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or  not spaceCheck(board, position):
            position = int(input('Choose your next position: (1-9) '))
        
    return position
            
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#Code for the game
print("WELCOME TO TIC TAC TOE GAME\n")
while True:
    newBoard = [' '] *10
    player1Marker, player2Marker = playerInput()
    turn = chooseFirst()
    print(turn + ' will go first.')
    
    playGame = input('\nAre you ready to play? Enter Yes or No.')
    
    if playGame.lower()[0] == 'y':
        gameOn = True
    else:
        gameOn = False
    while gameOn:
        if turn == 'Player 1':
            
            displayBoard(newBoard)
            print("\nPlayer 1's turn")
            pos = playerChoice(newBoard)
            placeMarker(newBoard,player1Marker,pos)
            
            if winCheck(newBoard,player1Marker):
                displayBoard(newBoard)
                print("CONGRATULATIONS PLAYER 1 WINS ")
                gameOn = False
            
            else:
                if fullBoardCheck(newBoard) :
                    displayBoard(newBoard)
                    print("AHH ITS A DRAW , TRY AGAIN")
                    break
                else:
                    turn = 'Player 2'
            
        else:
            
            print("\nPlayer 2's turn")
            displayBoard(newBoard)
            pos = playerChoice(newBoard)
            placeMarker(newBoard,player2Marker,pos)
            
            if winCheck(newBoard,player2Marker):
                displayBoard(newBoard)
                print("CONGRATULATIONS PLAYER 2 WINS ")
                gameOn = False
            
            else:
                if fullBoardCheck(newBoard) :
                    displayBoard(newBoard)
                    print("AHH ITS A DRAW , TRY AGAIN")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
      break
