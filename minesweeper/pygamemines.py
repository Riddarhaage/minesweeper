# import the pygame module, so you can use it
import pygame
import random
from collections import Counter

pygame.init()
# Create a window with the specified dimensions


# Set the caption of the window
pygame.display.set_caption("Minesweeper av Ruben Riddarhaage")

MINE = 10 # changed to 10 so pygame don't confuse my mines with the cells that have 1 adj mine
HIDDENCELL = -1
EMPTY = 0
FLAG = 'F'

boardSize = 20
width = boardSize*32 # the tiles are 32px in size
height = boardSize*32

pygame_icon = pygame.image.load("minesweeper\\img\\icon.png")
pygame.display.set_icon(pygame_icon)
screen = pygame.display.set_mode((width, height))

board = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
boardDisplay = [[-1 for _ in range(boardSize)] for _ in range(boardSize)]

num_mines = 50

for i in range(num_mines):
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board[0]) - 1)
    board[row][col] = MINE 

def draw(board, board_display):
    # Load the images for the cells
    empty_image = pygame.image.load("minesweeper\\img\\empty.png")
    mine_image = pygame.image.load("minesweeper\\img\\mine.png")
    flag_image = pygame.image.load("minesweeper\\img\\flag.png")
    hidden_image = pygame.image.load("minesweeper\\img\\hidden.png")
    adjMines1 = pygame.image.load("minesweeper\\img\\1.png")
    adjMines2 = pygame.image.load("minesweeper\\img\\2.png")
    adjMines3 = pygame.image.load("minesweeper\\img\\3.png")
    adjMines4 = pygame.image.load("minesweeper\\img\\4.png")
    adjMines5 = pygame.image.load("minesweeper\\img\\5.png")
    adjMines6 = pygame.image.load("minesweeper\\img\\6.png")
    adjMines7 = pygame.image.load("minesweeper\\img\\7.png")
    adjMines8 = pygame.image.load("minesweeper\\img\\8.png")

    # Calculate the size of each cell
    cell_width = screen.get_width() // len(board)
    cell_height = screen.get_height() // len(board)

    # Draw each cell on the screen
    for row in range(len(board)):
        for col in range(len(board[row])):
            x = col * cell_width
            y = row * cell_height
            if board_display[row][col] == MINE:
                screen.blit(mine_image, (x, y))
            elif board_display[row][col] == HIDDENCELL:
                screen.blit(hidden_image, (x, y))
            elif board_display[row][col] == "F":
                screen.blit(flag_image, (x, y))
            elif checkAdjCells(row, col) == 1:
                screen.blit(adjMines1, (x, y))
            elif checkAdjCells(row, col) == 2:
                screen.blit(adjMines2, (x, y))
            elif checkAdjCells(row, col) == 3:
                screen.blit(adjMines3, (x, y))
            elif checkAdjCells(row, col) == 4:
                screen.blit(adjMines4, (x, y))
            elif checkAdjCells(row, col) == 5:
                screen.blit(adjMines5, (x, y))
            elif checkAdjCells(row, col) == 6:
                screen.blit(adjMines6, (x, y))
            elif checkAdjCells(row, col) == 7:
                screen.blit(adjMines7, (x, y))
            elif checkAdjCells(row, col) == 8:
                screen.blit(adjMines8, (x, y))

            else:
                screen.blit(empty_image, (x, y))
                # Draw the number of adjacent mines if the cell is not empty
                
    # Update the display
    pygame.display.update()



def checkAdjCells(row,col):
    adjMines = 0
    r = row - 1
    while r <= row+1:
        if r>=0 and r <len(board):
            c = col - 1
            while c <= col + 1:
                if c>=0 and c<len(board):
                    adjMines += board[r][c]//10 # since mines = 10, it's divided by itself to add 1 mine to the count
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




hiddenCellCount = Counter(c for clist in boardDisplay for c in clist)

running = True
while running:
    #hiddenCellCount = Counter(c for clist in boardDisplay for c in clist)
    #if hiddenCellCount[-1] == num_mines:
     #   print("YOU WON!")
    # Pump and handle event
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
           #print(hiddenCellCount)
            mouse_pos = pygame.mouse.get_pos()
            # Calculate the row and column indices of the clicked cell
            cell_width = screen.get_width() // len(board)
            cell_height = screen.get_height() // len(board)
            col = mouse_pos[0] // cell_width
            row = mouse_pos[1] // cell_height
            # Update the game state and boardDisplay
            if event.button == 1:  # Left mouse button
                # Open the cell
                if boardDisplay[row][col] == FLAG:
                    pass
                elif board[row][col] == MINE:
                    # Game over
                    boardDisplay[row][col] = MINE
                    draw(board, boardDisplay)
                    print("You lost!")
                    pygame.time.wait(3000)
                    pygame.quit()
                
                else:
                    # Open the cell and display the number of adjacent mines
                    boardDisplay[row][col] = board[row][col]
                    
                if board[row][col] == EMPTY and boardDisplay[row][col] != FLAG:
                    # Open adjacent empty cells
                    openAdjEmpyCell(row, col)
            elif event.button == 3:  # Right mouse button
                # Flag the cell
                if boardDisplay[row][col] == FLAG:
                    boardDisplay[row][col] = HIDDENCELL
                else:
                    boardDisplay[row][col] = FLAG
            # Redraw the board
            draw(board, boardDisplay)
    
    draw(board, boardDisplay)