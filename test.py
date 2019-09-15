from tkinter import *
import numpy as np
import time



master = Tk()

boxNumberEnter = 300
boxNumber = boxNumberEnter
size = 1000
boxSize = size/boxNumber
n = int(boxNumberEnter/2)

aliveList = []
aliveList2 = []
grid = np.zeros((boxNumber,boxNumber)).astype('int')
grid[n][n] = 1
grid[n][n-1] = 1
grid[n][n-2] = 1
grid[n][n-3] = 1
grid[n][n-4] = 1
grid[n+4][n] = 1
grid[n+4][n-1] = 1
grid[n+4][n-2] = 1
grid[n+4][n-3] = 1
grid[n+4][n-4] = 1
grid[n+2][n-4] = 1
grid[n+2][n] = 1


w = Canvas(master, width=size, height=size)
w.pack()
for box in range(0, boxNumber):
    w.create_text((box*boxSize-boxSize/2)+boxSize, 20, text=str(box-1))
for box in range(0, boxNumber):
    w.create_text(20, (box * boxSize - boxSize / 2) + boxSize, text=str(box-1))


def create_rec(s, x, y):
    w.create_rectangle((x + 1) * boxSize, (y + 1) * boxSize, (x + 1) * boxSize + boxSize,
                   (y + 1) * boxSize + boxSize, fill=s, tags=(str(x) + "-" + str(y)))


def click(event):
    x, y = event.x, event.y
    if w.find_withtag(CURRENT):
        w.delete(str(int(x/boxSize)-1)+" "+str(int(y/boxSize)-1))
        create_rec("grey", int(x/boxSize)-1, int(y/boxSize)-1)
        aliveList2.append([int(x/boxSize)-1, int(y/boxSize)-1])
        aliveList.append([int(x / boxSize)-1, int(y / boxSize)-1])


def build_grid():
    for b in aliveList:
        for i in range(b[0]-1, b[0]+2):
            for j in range(b[1] - 1, b[1] + 2):
                num1 = 0
                if(i+1 < boxNumber and i-1 > 0 and j+1 < boxNumber and j-1 > 0):
                    num1 = grid[i + 1][j] + grid[i - 1][j] + grid[i + 1][j + 1] + grid[i - 1][j + 1] + grid[i - 1][j - 1] + \
                        grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j - 1]
                if num1 == 2:
                    if(grid[i][j]==1):
                        if [i, j] not in aliveList2:
                            aliveList2.append([i, j])
                if num1 == 3:
                    if [i, j] not in aliveList2:
                        aliveList2.append([i, j])

w.bind("<Button-1>", click)

w.create_rectangle(0, 0, boxSize, boxSize, fill="white")

num = 0


for i in range(0, boxNumber):
    for j in range(0, boxNumber):
        if grid[i][j] == 1:
            aliveList.append([i, j])
            create_rec("grey", i, j)
        else:
            create_rec("white", i, j)

master.update()

newGrid = np.zeros((boxNumber, boxNumber)).astype('int')
count = 0
frameCount = 0

t = time.time()

while True:
    frameCount+=1
    count+=1
    if count==1000:
        break
    build_grid()
    for b in aliveList:
        grid[b[0]][b[1]] = 0
        w.itemconfig(str(b[0]) + "-" + str(b[1]), fill="white")
    aliveList = aliveList2.copy()
    for b in aliveList:
        grid[b[0]][b[1]] = 1
        w.itemconfig(str(b[0]) + "-" + str(b[1]), fill="grey")
    aliveList2.clear()
    master.update()
print(time.time()-t)



