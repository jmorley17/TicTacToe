import random
import os

whitespace = ' ' #used in displaying and resetting board
GameTie = False
board = {  #dictionary corresponding to game board to be updated on each turn
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
    }       

class Player():
    
    def __init__(self, name) -> None:
        self.name = name
        self.winner = False

def choosePlayers():
    '''
    This function assigns names and markers to players. 
    It will create object of class Player based on the user's choices.
    '''
    global nameChoice
    global Player1
    global Player2
    #ask First user for name
    nameChoice = input("First player, what is your name? ")
    
    #stores name as object attribute
    Player1 = Player(nameChoice)
    Player1.name = nameChoice

    #ask First user for marker
    markChoice='wrong'
    while markChoice not in ['X','O']:
        markChoice = input("Please choose X or O ")
        if markChoice not in ['X','O']:
            print("Please choose X or O ")

    #store player one's marker as object attribute
    Player1.mark = markChoice

    #asks second user for name
    nameChoice = input("Second player, what is your name? ")

    #stores second user's name as object attribute
    Player2 = Player(nameChoice)
    Player2.name = nameChoice

    #assigns second player's marker attribute opposite of what the first player picked
    if Player1.mark == 'X':
      Player2.mark = 'O'
    elif Player1.mark == 'O':
      Player2.mark = 'X'

def display_board(board):
    '''
    This function prints the game board from dictionary "board".
    '''
    print(whitespace, board['7'], whitespace, '|', 
    whitespace, board['8'], whitespace, '|', 
    whitespace, board['9'], whitespace) 
    print("---------------------")
    print(whitespace, board['4'], whitespace, '|', 
    whitespace, board['5'], whitespace, '|', 
    whitespace, board['6'], whitespace) 
    print("---------------------")
    print(whitespace, board['1'], whitespace, '|', 
    whitespace, board['2'], whitespace, '|', 
    whitespace, board['3'], whitespace
    )

def chooseFirstPlayer():
    '''
    This will randomly choose a player to go first based on a flip.
    The result of the flip will assign T/F boolean to an attribute of the Player object for both players.
    It will also print who goes first for the user.
    '''
    os.system("cls")
    flip = random.randint(0,1)
    if flip == 0:
        Player1.turn = True
        Player2.turn = False
        print(Player1.name + " will go first.")
    elif flip == 1:
        Player2.turn = True
        Player1.turn = False
        print(Player2.name + " will go first.")

def toggle_players():
    '''
    This will toggle the turn attribute for both player objects.
    '''
    Player1.turn = not Player1.turn
    Player2.turn = not Player2.turn

def resetBoard():
    '''
    This function redefines the values for each position of the game board to a blank space.
    '''
    global board
    board = {  #dictionary corresponding to game board to be updated on each turn
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
    }         

def resetGame():
    '''
    This function combines the functions to reset the board, and choose who will go first.
    '''
    resetBoard()
    chooseFirstPlayer()

def askReplay():
    '''
    This function is run at the end of the game sequence if it ends in a win or draw, and controls the gameOn variable, which is the escape to the play loop.
    '''
    global gameOn

    #Asks user if they would like to keep playing. Verifies input is Y or N or continues to ask.
    keepPlaying = 'wrong'
    while keepPlaying not in ['Y','N']:
        keepPlaying = input("Would you like to play again? Y or N ")
        if keepPlaying not in ['Y','N']:
            print("Please enter Y or N")
    
    if keepPlaying == 'Y':
        gameOn = True
        os.system('cls')
        resetGame()
    else:
        gameOn = False

def displayWinner():
    '''
    This function is only called if the current player meets a win criteria. It prints that the user has won, and also assigns the object attribute that they have won.
    '''
    if Player1.turn:
        print(f"Congratulations {Player1.name}! You have won.")
        Player1.winner = True
    elif Player2.turn:
        print(f"Congratulations {Player2.name}! You have won.")
        Player2.winner = True
    askReplay()

def checkForWin():
    '''
    Determines wether to check for X's or O's based on whose turn it is
    Checks for each possible winning board
    Runs function displayWinner if the player has won.
    '''
    
    # determine which mark to check for
    if Player1.turn:
        marksToCheck = Player1.mark
    elif Player2.turn:
        marksToCheck = Player2.mark

    if marksToCheck == board['1'] == board['4'] == board['7']:
        displayWinner()
    elif marksToCheck == board['2'] == board['5'] == board['8']:
        displayWinner()
    elif marksToCheck == board['3'] == board['6'] == board['9']:
        displayWinner()
    elif marksToCheck == board['1'] == board['2'] == board['3']:
        displayWinner()
    elif marksToCheck == board['4'] == board['5'] == board['6']:
        displayWinner()
    elif marksToCheck == board['7'] == board['8'] == board['9']:
        displayWinner()
    elif marksToCheck == board['1'] == board['5'] == board['9']:
        displayWinner()
    elif marksToCheck == board['7'] == board['5'] == board['3']:
        displayWinner()
    else:
        return False

def checkForTie():
    '''
    This function checks if all spaces have been played. It is only run if a winner has not been declared.
    '''
    global GameTie
    if board['1'] != ' ' and board['2'] != ' ' and board['3'] != ' ' and board['4'] != ' ' and board['5'] != ' ' and board['6'] != ' ' and board['7'] != ' ' and board['8'] != ' ' and board['9'] != ' ':
        os.system('cls')
        display_board(board)
        print("Sorry, the game ended in a draw.")
        GameTie = True
        askReplay()
    else:
        pass

def userChoice():
    '''
    This function ask the current player which position on the board to play, and changes the dictionary board at that location to the player's marker.
    '''
    if Player1.turn:
        playerTurn = 'Player 1'
    elif Player2.turn:
        playerTurn = 'Player 2'
 
    playerChoice = 'wrong'
    while playerChoice not in ['1','2','3','4','5','6','7','8','9']:
        # playerChoice = input(f"{playerTurn} choose a keyboard position from 1 to 9: ")
        if Player1.turn:
            playerChoice = input(f"{Player1.name}, choose a keyboard position from 1 to 9: ")
        elif Player2.turn:
            playerChoice = input(f"{Player2.name}, choose a keyboard position from 1 to 9: ")

        # check if choice is a valid board position
        if playerChoice not in ['1','2','3','4','5','6','7','8','9']:
            print(f"{playerTurn} please choose a selection between 1 and 9.")
        
        # check if choice is already taken
        elif board[playerChoice] != ' ':
            playerChoice = 'wrong'
            print("That spot is already taken. Please choose another keypad location between 1 and 9.")
        
        # make a change to the board
        else:
            os.system('cls')
            if Player1.turn:
                board[playerChoice] = Player1.mark
            elif Player2.turn:
                board[playerChoice] = Player2.mark
            # display_board(board)
            
def gameIntro():
    '''
    Prints a welcome message and an overview of the board layout.
    '''
    print("Welcome to Tick Tac Toe!")
    print("The game board is based on your number keypad as shown below:")
    print(whitespace, '7', whitespace, '|', whitespace, '8', whitespace, '|', whitespace, '9', whitespace) 
    print("---------------------") 
    print(whitespace, '4', whitespace, '|', whitespace, '5', whitespace, '|', whitespace, '6', whitespace) 
    print("---------------------") 
    print(whitespace, '1', whitespace, '|', whitespace, '2', whitespace, '|', whitespace, '3', whitespace)

def gameSetup():
    '''
    This function establishes the initial setup of the board, and runs the functions to get the user's names and markers.
    '''
    gameIntro()
    choosePlayers()
    chooseFirstPlayer()

def gameSequence():
    '''
    Defines the game logic for game to cycle over until a winner or tie is declared.
    '''
    global GameTie
    display_board(board) #Prints board in current state
    userChoice() #Asks user for their play
    checkForWin() #Checks if the current player has won
    
    if Player1.winner != True and Player2.winner != True:
        checkForTie() #Checks if the game has ended in a draw
        if GameTie != True:
            toggle_players()

    #resets the winner attributes to False.
    Player1.winner = False
    Player2.winner = False
    GameTie = False

# Game Start
gameOn = True
gameSetup()

#this is the main loop to continue running the game sequence until gameOn is set to False.
while gameOn:

    gameSequence()