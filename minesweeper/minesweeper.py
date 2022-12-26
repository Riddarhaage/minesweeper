#%%
import random

def displayNakedBoard():
    value_symbol_map = {
        1: "*",
        0: " ",
        "F": "F"
    }
    print("  ", end="") 
    for col in range(0, 10):  # Print the column index
        print(f"\033[4m {col} \033[0m", end="")
    print("") 
    for row in range(0, 10):  # Print the row index
        print(f"{row}|", end="")
        for col in range(0, 10):
            symbol = value_symbol_map.get(board[row][col], " ")
            print(f"\033[4m{symbol}\033[0m", end="\033[4m" + " |" + "\033[0m")
        print("")

def displayBoard():
    print("  ", end="") 
    for col in range(0, 10):  # Print the column index
        print(f"\033[4m {col} \033[0m", end="")
    print("") 
    for row in range(0, 10):  # Print the row index
        print(f"{row}|", end="")
        for col in range(0, 10):
            if boardDisplay[row][col] == HIDDENCELL:
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
                if((boardDisplay[row][col]==HIDDENCELL) and (board[row][col]==EMPTY)):
                    boardDisplay[row][col] = checkAdjCells(row,col)

                    if checkAdjCells(row,col) == EMPTY and (row,col) not in cells:
                        cells.append((row,col))
                    else:
                        boardDisplay[row][col] = checkAdjCells(row,col)

def setFlag(row, col):
    if boardDisplay[row][col] == "F":
        boardDisplay[row][col] = HIDDENCELL
        
    else:
        boardDisplay[row][col] = "F"

    

MINE = 1
HIDDENCELL = -1
EMPTY = 0
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
        board[bombRow][bombCol] = MINE
    mines += 1


displayNakedBoard()
print("")
displayBoard()

complete = any(-1 in x for x in boardDisplay)
while complete:
    flag = input("place/remove flag?(y/n): ").lower()
    if flag == 'y':
        cell = input("pick a cell:")
        splitCell = cell.split(',')
        row = int(splitCell[0])
        col = int(splitCell[1])
        setFlag(row,col)
        displayBoard()
        complete = any(-1 in x for x in boardDisplay)
    elif flag == 'n':
        try:
            cell = input("pick a cell:")
            splitCell = cell.split(',')
            row = int(splitCell[0])
            col = int(splitCell[1])
        except:
            print("\u001b[31mERROR:\u001b[37m.Try to enter a valid row & column seperated by a comma")
        
        try:
            if boardDisplay[row][col] == 'F':
                print("Can't open a flagged cell!")
            elif board[row][col] == MINE:
                print("you lost!")
                displayNakedBoard()
                break
            else:
                boardDisplay[row][col] = openAdjEmpyCell(row, col)
                boardDisplay[row][col] = checkAdjCells(row, col)
                displayBoard()
                complete = any(-1 in x for x in boardDisplay)
        except:
            pass
print("Congratulations! you won!")