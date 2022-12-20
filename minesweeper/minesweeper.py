#%%
import random
from blessed import Terminal

def displayNakedBoard():
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            print(f"{board[row][col]}", end=" ")
        print("")

def displayBoard():
    test = " "
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            if boardDisplay[row][col] == hiddenCell:
                print("\033[4m" + " " + "\033[0m", end="\033[4m" + " |" + "\033[0m")
            else:
                print(f"{txtUnderline.join(boardDisplay[row][col])}", end=" |")
        print("")
txtUnderline = "\033["
endUnderline = "\033[0m"
bomb = 1
hiddenCell = -1  
        #row and cols 10x10 grid
        #not visible to user
board = [
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
                              ]
        #same size grid that will be visible to the user
boardDisplay = [
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                                        ]


numOfMines = int(input("Amount of mines: "))
if numOfMines == 0:
    numOfMines = 5
    print("not enought mines to make things interesting!")
    print(f"{numOfMines} mines added to the board")
if numOfMines > 75:
    numOfMines = 75
    print("Woah! that's way too many mines!")
    print(f"Luckily I only added {numOfMines} mines to the board!")

mines = 0
while mines < numOfMines:
    bombRow = random.randint(0, len(board)-1)
    bombCol = random.randint(0, len(board)-1)
    if board[bombRow][bombCol] == 0:
        board[bombRow][bombCol] = bomb
    mines += 1


displayNakedBoard()
displayBoard()