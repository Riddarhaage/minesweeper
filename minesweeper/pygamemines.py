# import the pygame module, so you can use it
import pygame
import random
from collections import Counter

pygame.init()
# Set the caption of the window
pygame.display.set_caption("Minesweeper av Ruben Riddarhaage")

MINE = 10 # changed to 10 so pygame don't confuse my mines with the cells that have 1 adj mine
HIDDENCELL = -1
EMPTY = 0
FLAG = 'F'

boardSize = 20
width = boardSize*32 # the tiles are 32px in size
height = boardSize*32

font = pygame.font.Font('freesansbold.ttf', 18)
pygame_icon = pygame.image.load("minesweeper\\img\\icon.png")
pygame.display.set_icon(pygame_icon)
screen = pygame.display.set_mode((width, height))
screen.fill((125,125,125))

board = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
boardDisplay = [[-1 for _ in range(boardSize)] for _ in range(boardSize)]

num_mines = 3
mines_input = pygame.Rect(200, 280, 240, 32)
# Set up the placeholder text for the input field
placeholder_text = font.render("Enter number of mines", True, (0,0,0))
placeholder_text_rect = placeholder_text.get_rect()
placeholder_text_rect.center = mines_input.center

# Set up the board size input box
board_size_input = pygame.Rect(200, 280, 240, 32)
board_size_ph_text = font.render("Enter Board Size", True, (0,0,0))
board_size_ph_rect = board_size_ph_text.get_rect()
board_size_ph_rect.center = board_size_input.center

# Set up the text input fields for the number of mines and board size
mines_text = ""
board_size_text = ""

# Set up a flag to track whether the input field is focused
mines_input_focused = False
board_size_input_focused = False
# Set up a flag to track whether the main menu is being displayed
display_main_menu = True
while display_main_menu:
    # Update the num_mines variable based on the user's input
    try:
        num_mines = int(mines_text)
    except ValueError:
        num_mines = 15
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the input field
            if mines_input.collidepoint(event.pos):
                mines_input_focused = True
            else:
                mines_input_focused = False
        if event.type == pygame.KEYDOWN:
            # Update the input field's text if it's focused
            if mines_input_focused:
                if event.key == pygame.K_BACKSPACE:
                    mines_text = mines_text[:-1]
                if event.key == pygame.K_RETURN:
                    # Try to convert the value of mines_text to an integer
                    # and update num_mines with it
                    try:
                        num_mines = int(mines_text) if mines_text.isdigit() else num_mines

                        # You can also add a check here to make sure that num_mines
                        # is within a valid range (e.g. 1 <= num_mines <= boardSize**2)
                        display_main_menu = False
                    except ValueError:
                        # If the conversion fails, set num_mines to a default value
                        # or display an error message to the user
                        num_mines = 15
                        display_main_menu = False
                else:
                    mines_text += event.unicode
            else:
                mines_text = ""  # Clear the input field if it's not focused
    
    # Render the input field's text
    mines_input_text = font.render(mines_text, True,(0,0,0))
    mines_input_text_rect = mines_input_text.get_rect()
    mines_input_text_rect.center = mines_input.center
    
    # Clear the screen
    screen.fill((125,125,125))
    
    # Draw the input field and text
    
    pygame.draw.rect(screen, (90,95,255), mines_input)
    if mines_input_focused:
        screen.blit(mines_input_text, mines_input_text_rect)
    else:
        screen.blit(placeholder_text, placeholder_text_rect)
    # Update the display
    pygame.display.flip()

display_size_menu = True
while display_size_menu:
    # Update the num_mines variable based on the user's input
    try:
        boardSize = int(board_size_text)
    except ValueError:
        boardSize = 20
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on the input field
            if board_size_input.collidepoint(event.pos):
                board_size_input_focused = True
            else:
                board_size_input_focused = False
        if event.type == pygame.KEYDOWN:
            # Update the input field's text if it's focused
            if board_size_input_focused:
                if event.key == pygame.K_BACKSPACE:
                    board_size_text = board_size_text[:-1]
                if event.key == pygame.K_RETURN:
                    # Try to convert the value of mines_text to an integer
                    # and update num_mines with it
                    try:
                        boardSize = int(board_size_text) if board_size_text.isdigit() else boardSize

                        # You can also add a check here to make sure that num_mines
                        # is within a valid range (e.g. 1 <= num_mines <= boardSize**2)
                        display_size_menu = False
                    except ValueError:
                        # If the conversion fails, set num_mines to a default value
                        # or display an error message to the user
                        boardSize = 10
                        display_size_menu = False
                else:
                    board_size_text += event.unicode
            else:
                board_size_text = ""  # Clear the input field if it's not focused
    
    # Render the input field's text
    board_size_input_text = font.render(board_size_text, True,(0,0,0))
    board_size_input_text_rect = board_size_input_text.get_rect()
    board_size_input_text_rect.center = board_size_input.center
    
    # Clear the screen
    screen.fill((125,125,125))
    
    # Draw the input field and text
    pygame.draw.rect(screen, (90,95,255), board_size_input)
    if board_size_input_focused:
        screen.blit(board_size_input_text, board_size_input_text_rect)
    else:
        screen.blit(board_size_ph_text, board_size_ph_rect)
    # Update the display
    pygame.display.flip()


width = boardSize*32 # the tiles are 32px in size
height = boardSize*32
screen = pygame.display.set_mode((width, height))
board = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
boardDisplay = [[-1 for _ in range(boardSize)] for _ in range(boardSize)]

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


PlayGame = True
while PlayGame:
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