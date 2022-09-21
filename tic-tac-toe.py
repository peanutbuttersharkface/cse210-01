print("Tic Tac Toe")
#W01 Prove:Developer
#Alicia Thompson

print()



print("Do you want to be player 1 or player 2?")
variable1 = input()
print("Welcome you will be player " + variable1 + "!")
while variable1 == "1":  
    print("You are x's.")
    print("Player 2 is o's.")
    break   
        
 
while variable1 == "2":
    print("You are o's.")
    print("Player 1 is x's.")    
    break

theBoard = {'1': '1' , '2': '2' , '3': '3' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '7': '7' , '8': '8' , '9': '9' }

board_keys = []

for key in theBoard:
    board_keys.append(key)



def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# main function 
def main():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print(turn + "'s turn to choose a square(1-9):")

        move = input()        

        if theBoard[move] in ('1', '2' , '3' , '4' , '5' , '6' , '7' , '8' ,'9') :
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")                
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("Good game. Thanks for playing")                
                print(turn + " won.")
                break 

        # If neither X nor O wins and the board is full, the result as 'tie'.
        if count == 9:
            print("Good game. Thanks for playing")                
            print("It's a Tie!!")

        # change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
if __name__ == "__main__":
    main()
