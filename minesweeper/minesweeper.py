#%%
import random
from blessed import Terminal

def displayNakedBoard():
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            print(f"\033[4m{board[row][col]}\033[0m",  end="\033[4m" + "|" + "\033[0m")
        print("")

def displayBoard():
    test = " "
    print("______________________________")
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            if boardDisplay[row][col] == hiddenCell:
                print("\033[4m" + " " + "\033[0m", end="\033[4m" + " |" + "\033[0m")
            else:
                print(f"\033[4m{boardDisplay[row][col]}\033[0m", end="\033[4m" + " |" + "\033[0m")
        print("")

def checkAdjCells(row,col):
    adjMines = 0
    r = row - 1
    while r <= row+1:
        if r>=0 and r <5:
            c = col - 1
            while c <= col + 1:
                if c>=0 and c<5:
                    adjMines += board[r][c] # 1 added to adjMines since mines = 1 on the board
                c += 1
        r += 1
    return adjMines

def openAdjEmpyCell(row, col):
    r = row - 1
    while r <= row+len(board):
        if r>=0 and r <len(board):
            c = col - 1
            while c <= col + len(board):
                if c>=0 and c<len(board):
                    if board[r][c] == 0:
                       _ = boardDisplay[r][c] = 0
                    elif board[r][c] != 0:
                        test = checkAdjCells(row,col)
                        return test
                c += 1
        r += 1
    return _

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
    numOfMines = 1
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

picks = 0

while picks < (100-numOfMines):
    print("example: '0,0'")
    cell = input("pick a cell:")
    splitCell = cell.split(',')
    row = int(splitCell[0])
    col = int(splitCell[1])
    if board[row][col] == bomb:
        print("you lost!")
        displayNakedBoard()
    else:
        boardDisplay[row][col] = openAdjEmpyCell(row, col)
        boardDisplay[row][col] = checkAdjCells(row,col)
        displayBoard()
    