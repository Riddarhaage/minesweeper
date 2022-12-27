#%%
import random
import time

MINE = 1
HIDDENCELL = -1
EMPTY = 0
REDTEXT = '\u001b[31m'
GREENTEXT = '\u001b[32m'
YELLOWTEXT = '\u001b[33m'
BLUETEXT =  '\u001b[34m'
MAGTEXT = '\u001b[35m'
CYANTEXT = '\u001b[36m'
RESETTEXT = '\u001b[0m'

def displayNakedBoard():
    value_symbol_map = {
        1: "*",
        0: " ",
        "F": "F"
    }
    print("    ", end="") 
    for col in range(0, len(board)):  # Print the column index
        print(f"\033[4m {col:2}\033[0m", end="")
    print("") 
    for row in range(0, len(board)):  # Print the row index
        print(f"{row:4}|", end="")
        for col in range(0, len(board)):
            symbol = value_symbol_map.get(board[row][col], " ")
            print(f"\033[4m{symbol}\033[0m", end="\033[4m" + " |" + "\033[0m")
        print("")


def displayBoard():
    print("    ", end="") 
    for col in range(0, len(board)):  # Print the column index
        print(f"\033[4m {col:2}\033[0m", end="")
    print("") 
    for row in range(0, len(board)):  # Print the row index
        print(f"{row:4}|", end="")
        for col in range(0, len(board)):
            if boardDisplay[row][col] == HIDDENCELL:
                print("\033[4m" + " " + "\033[0m", end="\033[4m" + " |" + "\033[0m")
            else:
                print(f"\033[4m{boardDisplay[row][col]}\033[0m", end="\033[4m" + " |" + "\033[0m")
        print("")


def checkAdjCells(row,col):
    adjMines = 0
    r = row - 1
    while r <= row+1:
        if r>=0 and r <len(board):
            c = col - 1
            while c <= col + 1:
                if c>=0 and c<len(board):
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
            if((row>=0 and row<=len(board)-1) and (col>=0 and col<=len(board)-1)):
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


boardSize = int(input("How many rows and columns do u want: "))
if boardSize > 51:
    boardSize = 51
    print(f"MAX board size is {boardSize} rows and columns")
if boardSize < 5:
    boardSize = 5
    print(f"Minimum board size in {boardSize} rows and columns")
board = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
boardDisplay = [[-1 for _ in range(boardSize)] for _ in range(boardSize)]

numOfMines = None
while numOfMines == None:
    try:
        numOfMines = int(input("Amount of mines: "))

        if numOfMines == 0:
            numOfMines = 1
            print("not enought mines to make things interesting!")
            print(f"{numOfMines} mines added to the board")
        if numOfMines > int(len(board)*len(board)*0.5):
            numOfMines = int(len(board)*len(board)*0.5)
            print("Woah! that's way too many mines!")
            print(f"Luckily I only added {numOfMines} mines to the board!")
    except:
        print(f"{REDTEXT}ERROR:{RESETTEXT} not a valid input!")

mines = 0
while mines < numOfMines:
    bombRow = random.randint(0, len(board)-1)
    bombCol = random.randint(0, len(board)-1)
    if board[bombRow][bombCol] == 0:
        board[bombRow][bombCol] = MINE
    mines += 1


#displayNakedBoard() #Prints the location of all the Mines for testing purposes
print("")
displayBoard()
HiddenCellsLeft = any(-1 in x for x in boardDisplay) #True
while HiddenCellsLeft:
    flag = input("place/remove flag?(y/n): ").lower()
    if flag == 'y':
        cell = input("pick a cell:")
        splitCell = cell.split(',')
        row = int(splitCell[0])
        col = int(splitCell[1])
        setFlag(row,col)
        displayBoard()
        HiddenCellsLeft = any(-1 in x for x in boardDisplay)
    elif flag == 'n':
        try:
            cell = input("pick a cell:")
            splitCell = cell.split(',')
            row = int(splitCell[0])
            col = int(splitCell[1])
        except:
            print(f"{REDTEXT}ERROR:{RESETTEXT} Try to enter a valid row & column seperated by a comma")
    elif flag == 'exit':
        break
        
    try:
        if boardDisplay[row][col] == 'F':
            print("Can't open a flagged cell!")
        elif board[row][col] == MINE:
            displayNakedBoard()
            for i in range(1,6):
                print(f"{REDTEXT}YOU HIT A MINE! YOU LOST!!!!!!{RESETTEXT}")
                time.sleep(0.2)
            break
        else:
            boardDisplay[row][col] = openAdjEmpyCell(row, col)
            boardDisplay[row][col] = checkAdjCells(row, col)
            displayBoard()
            HiddenCellsLeft = any(-1 in x for x in boardDisplay)
    except:
        pass
if HiddenCellsLeft == False:
    for i in range(1, 10):
        print(f"{GREENTEXT}CONGR{CYANTEXT}ATULATIONS {REDTEXT}YOU {GREENTEXT} WON{CYANTEXT}!!!{REDTEXT}!!!{RESETTEXT}")
        time.sleep(0.3)