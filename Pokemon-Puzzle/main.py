import pygame as pg
import os
import sys
import cfg  # Configuration file that we have created for Game 
import random   # helps to generate random numbers for choosing random images

# Game Over Function 
def isGameOver(board, size):
    # Checking if the size of our game is right type or not
    assert isinstance(size, int)
    # If we get right time, isinstance() method will return true and code will get further executing
    # This is generally done to ensure that, game would run smoothly

    # Defining the Number of Cells in Game 
    numCells = size * size  # vertical size * horizontal size

    # Checking Every Cells in Game
    for i in range(numCells - 1):
        if board[i] != i: return False
        # Here, board[i]: is the cell that is in the board
        # And, i is the actual cell in the image 
    return True  # isGameOver() will be activated 


# Defining Control Functions (Moves) in Puzzle Game
# Move Right
def moveRight(board, blankCellInd, numCols):
    if (blankCellInd % numCols == 0): 
        return blankCellInd
    board[blankCellInd - 1], board[blankCellInd] = board[blankCellInd], board[blankCellInd - 1]
    return blankCellInd - 1

# Move Left
def moveLeft(board, blankCellInd, numCols):
    if ((blankCellInd + 1) % numCols == 0): 
        return blankCellInd
    board[blankCellInd + 1], board[blankCellInd]=board[blankCellInd], board[blankCellInd + 1]
    return blankCellInd + 1

# Move Down
def moveDown(board, blankCellInd, numCols):
    if (blankCellInd < numCols):
        return blankCellInd
    board[blankCellInd - numCols], board[blankCellInd]=board[blankCellInd], board[blankCellInd - numCols]
    return blankCellInd - numCols

# Move Up
def moveUp(board, blankCellInd, numRows, numCols):
    if (blankCellInd >= ((numRows - 1) * numCols)): 
        return blankCellInd
    board[blankCellInd + numCols], board[blankCellInd]=board[blankCellInd], board[blankCellInd + numCols]
    return blankCellInd + numCols


# Creating Board for the Game
def CreateBoard(numRows, numCols, numCells):
    board=[]    # Defining board as an empty list
    # Loop that basically fill the board list
    for i in range(numCells): board.append(i)
    blankCellInd=numCells-1
    board[blankCellInd]=-1

    # Providing Directions according to the number
    # Poviding Direction Controls 
    for i in range(cfg.randomNum):
        # Providing directions according to number
        direction=random.randint(0, 3)  # Here, each number is the direction (left, right, up and down),coordinates
        if (direction==0):
            blankCellInd=moveLeft(board, blankCellInd, numCols)
        elif (direction==1):
            blankCellInd=moveRight(board, blankCellInd, numCols)
        elif (direction==2):
            blankCellInd=moveUp(board, blankCellInd, numRows, numCols)
        elif(direction==3):
            blankCellInd=moveDown(board, blankCellInd, numCols)
        else:
            print("Invalid Input")
    return board, blankCellInd


# Getting Image from our files
def GetImagePath(rootDir):
    imgNames=os.listdir(rootDir)
    # Checking, whether our file is okay or not
    assert len(imgNames) > 0
    return os.path.join(rootDir, random.choice(imgNames))


# Defining Screen Interface on Endings
def ShowEndInterface(screen, width, height):
    screen.fill(cfg.bgColor)
    font=pg.font.Ffont(cfg.fontPath, width//15)
    title=font.render("Good Job! You Won...", True, (233, 150, 122))
    rect=title.get_rect()
    rect.midtop=(width/2, height/2.5)
    screen.blit(title, rect)
    pg.display.update()
    # Condition to exit the game: 
    while True: 
        for event in pg.event.get():
            if ((event.type==pg.QUIT) or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
        pg.display.update()


# Defining Screen Interface on Starting 
def ShowStartInterface(screen, width, height):
    screen.fill(cfg.bgColor)
    tFont=pg.font.Font(cfg.boldFontPath, width//10)
    cFont=pg.font.Font(cfg.fontPath, width//20)
    title=tFont.render("Pokemon Puzzle", True, cfg.Red)
    content1=cFont.render("Press H, M or L to choose your Puzzle...", True, cfg.Blue)
    content2=cFont.render("H - 5X5, M - 4X4, L - 3X3", True, cfg.Blue)
    trect=title.get_rect()
    trect.midtop=(width/2, height/5)
    crect1=content1.get_rect()
    crect1.midtop=(width/2, height/2.2)
    crect2=content2.get_rect()
    crect2.midtop=(width/2, height/1.8)
    screen.blit(title, trect)
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    while True:
        for event in pg.event.get():
            if((event.type==pg.QUIT) or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            elif(event.type==pg.KEYDOWN):
                if(event.key==ord("l")): return 3
                elif(event.key==ord("m")): return 4
                elif(event.key==ord("h")): return 5
        pg.display.update()


# Defining our main() clause
def main():
    # Initializing our Game 
    pg.init()
    # Setting up a Clock
    clock=pg.time.Clock()
    # Setting up the images that's going to be used. 
    imgUsed=pg.image.load(GetImagePath(cfg.imgRootDir))
    imgUsed=pg.transform.scale(imgUsed, cfg.ScreenSize)
    # Creating Rectangle Around the Pictures
    imgUsedRect=imgUsed.get_rect()

    screen=pg.display.set_mode(cfg.ScreenSize)
    pg.display.set_caption("Pokemon Puzzle Game")
    size=ShowStartInterface(screen, imgUsedRect.width, imgUsedRect.height)
    assert isinstance(size, int)    # Ensuring Screen Size as Integers
    numRows, numCols=size, size
    numCells=size*size
    # Cell Size
    cellWidth=imgUsedRect.width//numCols
    cellHeight=imgUsedRect.height//numRows

    while True: 
        gameBoard, blankCellInd=CreateBoard(numRows, numCols, numCells)
        if not isGameOver(gameBoard, size):
            break

    # Because the game isn't over until it is played 
    is_running=True

    while is_running:
        for event in pg.event.get():
            if (event.type==pg.QUIT) or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            # KeyBoard Controls 
            elif (event.type==pg.KEYDOWN):
                if (event.key==pg.K_LEFT or event.key==ord("a")):
                    blankCellInd==moveLeft(gameBoard, blankCellInd, numCols)
                elif (event.key==pg.K_RIGHT or event.key == ord('d')):
                    blankCellInd==moveRight(gameBoard, blankCellInd, numCols)
                elif (event.key==pg.K_UP or event.key == ord('w')):
                    blankCellInd==moveUp(gameBoard, blankCellInd, numRows, numCols)
                elif (event.key==pg.K_DOWN or event.key == ord('s')):
                    blankCellInd==moveDown(gameBoard, blankCellInd, numCols)

            # Mouse Control
            elif (event.type==pg.MOUSEBUTTONDOWN and event.button==1):
                x, y= pg.mouse.get_pos()
                xPos=x//cellWidth
                yPos=y//cellHeight

                # Creating index
                index=xPos+yPos*numCols
                if (index == blankCellInd-1):
                    blankCellInd = moveRight(gameBoard, blankCellInd, numCols)
                elif (index == blankCellInd+1):
                    blankCellInd = moveLeft(gameBoard, blankCellInd, numCols)
                elif (index == blankCellInd + numCols):
                    blankCellInd = moveUp(gameBoard, blankCellInd, numRows, numCols)
                elif (index == blankCellInd - numCols):
                    blankCellInd = moveDown(gameBoard, blankCellInd, numCols)

        if isGameOver(gameBoard, size):
            gameBoard[blankCellInd] = numCells - 1
            is_running = False
            
        # Updating the Screen 
        screen.fill(cfg.bgColor)
        for i in range(numCells):
            if gameBoard[i] == -1: continue
            xPos=i//numCols
            yPos=i%numCols

            # Creating Rectangle
            rect = pg.Rect(yPos*cellWidth, xPos*cellHeight, cellWidth, cellHeight)
            imgArea=pg.Rect((gameBoard[i]%numCols)*cellWidth, (gameBoard[i]//numCols)*cellHeight, cellWidth, cellHeight)
            screen.blit(imgUsed, rect, imgArea)

        # Defining Cell Border Width
        borderWidth=3

        # Defining Particular Color for Identifying the Blank Cell
        blankCellColor=cfg.Blank
        blankCellRect=pg.Rect((blankCellInd%numCols)*cellWidth, (blankCellInd//numCols)*cellHeight, cellWidth, cellHeight)
        screen.fill(blankCellColor, blankCellRect)

        for i in range(numCols+1):
            pg.draw.line(screen, cfg.Black, (i*cellWidth, 0), (i*cellWidth, imgUsedRect.height), borderWidth)
        for i in range(numRows+1):
            pg.draw.line(screen, cfg.Black, (0, i*cellHeight), (imgUsedRect.width, i*cellHeight), borderWidth)
        
        # Adding the screen border
        borderColor = cfg.Black
        borderWidth = 5
        pg.draw.rect(screen, borderColor, (0, 0, imgUsedRect.width, imgUsedRect.height), borderWidth)

        pg.display.update()
        clock.tick(cfg.fps)
    ShowEndInterface(screen, imgUsedRect.width, imgUsedRect.height)


# Writing run statements, which will generally run our main function
# Simply, it runs our program 
if __name__=="__main__":
    main()