#  File: KTV1.py

#  Description: Knight's Tour

#  Student Name: Russell Kan

#  Student UT EID: rjk854

#  Course Name: lul

#  Unique Number: heh

#  Date Created:7-11-17

#  Date Last Modified: 7-11-17

from graphics import *

def drawBoard(win):
    board = Rectangle(Point(25,75), Point(505,555))
    board.setFill("white")
    board.draw(win)
    # Draw horizontal lines
    for row in range(0,8):
        for col in range(0,8):
            top = Point(row*60+25, col*60+75)
            bottom = Point((row+1)*60+25, (col+1)*60+75)
            tile = Rectangle(top,bottom)
            if (row+col)%2 == 0:
                color = color_rgb(251,201,159)
            else:
                color = color_rgb(210,136,70)
            tile.setFill(color)
            tile.draw(win)

def countMoves(board, numBoard, moves, x, y):
    for d in range(len(board[0])):
        for c in range(len(board[0])):
            count = 0
            for move in moves:
                if isValid(board, move, c, d):
                    count += 1
            numBoard[d][c] = count

def findTile(pt):
    # Change point coordinates into location on board
    x = int((pt.getX() - 25)/60)
    y = int((pt.getY() - 75)/60)
    return (x, y)

def findPixel(x, y):
    return Point(x*60+55,y*60+105)

def makeMove(board, win, x, y):
    board[y][x] = 1
    center = findPixel(x, y)
    center.draw(win)
    x1 = Line(Point(center.getX()-15, center.getY()-15), Point(center.getX()+15, center.getY()+15))
    x2 = Line(Point(center.getX()-15, center.getY()+15), Point(center.getX()+15, center.getY()-15))
    x1.setWidth(4)
    x2.setWidth(4)
    x1.draw(win)
    x2.draw(win)

def isValid(board, move, x, y): # check if a move is valid
    if x+move[0] >= 0 and y+move[1] >= 0 and x+move[0] < 8 and y+move[1] < 8:   # check boundaries
        if board[y+move[1]][x+move[0]] != 1:    # check if a space has been visited already
            return True
    else:
        return False

def step(board, numBoard, win, moves, x, y, rgb):
    lowest = 8
    for move in moves:
        if isValid(board, move, x, y):
            if numBoard[y+move[1]][x+move[0]] <= lowest:
                newX = x + move[0]
                newY = y + move[1]
                lowest = numBoard[newY][newX]
                nextMove = move

    oldCenter = findPixel(x, y)
    newCenter = findPixel(newX, newY)
    line = Line(Point(oldCenter.getX(), oldCenter.getY()), Point(newCenter.getX(), newCenter.getY()))
    line.setWidth(2.5)
    color = color_rgb(rgb[0], rgb[1], rgb[2])
    line.setFill(color)
    line.draw(win)

    makeMove(board, win, newX, newY)
    countMoves(board, numBoard, moves, x, y)

    print("board of moves:")
    for a in numBoard:
        print(a)
    print("next move", nextMove, "to [", newX, ",", newY, "]")

    input("press any key...")
    return newX, newY


def main():
    board = [[0 for y in range(8)] for x in range(8)]
    numBoard = [[0 for y in range(8)] for x in range(8)]
    moves = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]    # possible moves of a knight

    win = GraphWin('Knight\'s Tour', 530, 580)
    win.setBackground('white')
    message = Text(Point(win.getWidth()/2, 30), 'Knight\'s Tour Version 1') 
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    drawBoard(win)
    
    p1 = Point(0,0)
    while p1.getX() < 25 or p1.getX() > 505 or p1.getY() < 75 or p1.getY() > 555:
        p1 = win.getMouse() # returns point of mouse click

    x, y = findTile(p1)
    makeMove(board, win, x, y)
    countMoves(board, numBoard, moves, x, y)
    rgb = [0, 0, 0]

    while True:
        x, y = step(board, numBoard, win, moves, x, y, rgb)

        if rgb[2] < 248:
            rgb[2] += 8
        else:
            rgb[0] += 8
            rgb[1] += 8
            

        if all(v == 1 for r in board for v in r):
            break

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
