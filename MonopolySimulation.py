import random
import matplotlib.pyplot as plt


def removeNewLines(board):
    boardClean =[]
    for x in board:
        x = x.rstrip("\n")
        boardClean.append(x)
    board = boardClean
    return board

def newGame():
    #get board from file
    inFile = open("Monopoly", "r")
    board = []
    board= inFile.readlines() #returns a list
    inFile.close()
    board = removeNewLines(board)
    
    #intialize board visits @ zero
    boardVisits = {}
    for x in range(len(board)):
        boardVisits[x] = 0
    
    #intialize player locations @ zero
    playerLocations = { "p1":0, "p2":0, "p3":0}
    return board, boardVisits, playerLocations

def displayVisits(boardVisits, board):
    xCor = []
    yCor = []
    for key in boardVisits:
        xCor.append(key)
        yCor.append(boardVisits[key])
    plt.bar(xCor, yCor, 1)
    plt.show()
#    for key in boardVisits:
#        print(format(str(boardVisits[key]), "5"), end ="")
#        print(board[key])

def setVisits(boardVisits, playerLocations):
    p1 = playerLocations["p1"]
    p2 = playerLocations["p2"]
    p3 = playerLocations["p3"]
    boardVisits[p1] += 1
    boardVisits[p2] += 1
    boardVisits[p3] += 1
    return boardVisits

def roll(doubleCount):
    first = random.randint(1,6)
    second = random.randint(1,6)
#    if (first == second):
#        doubleCount += 1
#        if (doubleCount < 3 ):
#            print(str(first), str(second), end=" ")
#            roll(doubleCount)
#        else:
#            print("go to jail")
    return first + second

def main():
    board, boardVisits, playerLocations = newGame()
    for turn in range (1000):
        playerLocations["p1"] += roll(0)
        playerLocations["p1"] = playerLocations["p1"]%40
        playerLocations["p2"] += roll(0)
        playerLocations["p2"] = playerLocations["p2"]%40
        playerLocations["p3"] += roll(0)
        playerLocations["p3"] = playerLocations["p3"]%40
        boardVisits = setVisits(boardVisits, playerLocations)   

    
    displayVisits(boardVisits, board)

main()





