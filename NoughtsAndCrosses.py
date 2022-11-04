#IMPORTS
import os
import time

#FUNCTIONS
def place(xCo,yCo):
    if int(xCo) > 3 or int(yCo) > 3 or board[3-int(yCo)][int(xCo)-1] in ['X', 'O']:
        return False
    if plr1Turn:
        board[3-int(yCo)][int(xCo)-1] = plr1
        return True
    else:
        board[3-int(yCo)][int(xCo)-1] = plr2
        return True

def checkWin(check):
    if board[0][0] == board[0][1] == board[0][2] == check or board[0][0] == board[1][0] == board[2][0] == check:
        return True
    if board[1][0] == board[1][1] == board[1][2] == check or board[0][1] == board[1][1] == board[2][1] == check:
        return True
    if board[2][0] == board[1][1] == board[0][2] == check or board[0][0] == board[1][1] == board[2][2] == check:
        return True
    if board[2][0] == board[2][1] == board[2][2] == check or board[0][2] == board[1][2] == board[2][2] == check:
        return True
    return False
        
def boardDisplay():
    print(str(board[0]) + "\n")
    print(str(board[1]) + "\n")
    print(str(board[2]) + "\n")
        

#MAIN

while True:
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

    plr1 = input("Player 1 pick X or O: ")
    while not plr1 in ['X', 'O', 'Y']:
        plr1 = input("Invalid \nPlayer 1 pick X or O: ")

    if plr1 == "Y":
        exit("Exiting...")

    if plr1 == 'X':
        plr2 = 'O'
    else:
        plr2 = 'X'

    plr1Turn = True

    for x in range(9):
        boardDisplay()
        if plr1Turn:
            print("Player 1's Turn")
        else:
            print("Player 2's Turn")
            
        while not place(input("Enter X co-ord: "),input("Enter Y co-ord: ")):
            print("Invalid")
        if plr1Turn:
            if checkWin(plr1):
                boardDisplay()
                print("Player 1(" + plr1 +  ") Wins!")
                break
        else:
            if checkWin(plr2):
                boardDisplay()
                print("Player 2(" + plr2 + ") Wins!")
                break

        if not plr1Turn:
            plr1Turn = True
        else:
            plr1Turn = False

        os.system('CLS')

    if (not checkWin(plr1)) and (not checkWin(plr2)):
        print("Draw!")

    time.sleep(3)
    os.system('CLS')



    

