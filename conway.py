#simple Conway's Game of Life program

import time, random, copy

WIDTH = 60
HEIGHT = 20

nextCells = []
for i in range(WIDTH):
    column = []
    for j in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') #add a living cell
        else:
            column.append(' ') #add a dead cell
    nextCells.append(column)

while True: #main program loop
    # print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    #print current cells on screen
    for i in range(WIDTH):
        for j in range(HEIGHT):
            print(currentCells[i][j], end='') #print the cell
    print() #print a newline

    # Calculate the next step's cells based on current step's cells:
    for i in range(WIDTH):
        for j in range(HEIGHT):
            #get neighbors
            leftCoord  = (i - 1) % WIDTH
            rightCoord = (i + 1) % WIDTH
            aboveCoord = (j - 1) % HEIGHT
            belowCoord = (j + 1) % HEIGHT

            #count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[i][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][j] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][j] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[i][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[i][j] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[i][j] = '#'
            elif currentCells[i][j] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[i][j] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[i][j] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.