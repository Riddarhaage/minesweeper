#%%
import random

def displayNakedBoard():
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            print(f"\033[4m{board[row][col]}\033[0m", end="\033[4m" + " |" + "\033[0m")
        print("")
            
        """print(f"\033[4m{board[row][col]}\033[0m",  end="\033[4m" + "|" + "\033[0m")
        print("")
        """

def displayBoard():
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
        if r>=0 and r <10:
            c = col - 1
            while c <= col + 1:
                if c>=0 and c<10:
                    adjMines += board[r][c] # 1 added to adjMines since mines = 1 on the board
                c += 1
        r += 1
    return adjMines

def openAdjEmpyCell(row, col):
    cells = [(row, col)]
    offsets = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
        
    while len(cells) > 0:
        cell = cells.pop()
        for offset in offsets:
            row = offset[0] + cell[0]
            col = offset[1] + cell[1]
            if((row>=0 and row<=9) and (col>=0 and col<=9)):
                if((boardDisplay[row][col]==hiddenCell) and (board[row][col]==empty)):
                    boardDisplay[row][col] = checkAdjCells(row,col)

                    if checkAdjCells(row,col) == empty and (row,col) not in cells:
                        cells.append((row,col))
                    else:
                        boardDisplay[row][col] = checkAdjCells(row,col)
    #displayBoard()
    

bomb = 1
hiddenCell = -1
empty = 0
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
        boardDisplay[row][col] = checkAdjCells(row, col)
        displayBoard()
    