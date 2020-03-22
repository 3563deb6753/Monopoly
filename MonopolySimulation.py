import random
import matplotlib.pyplot as plt


PLAYERS = 3

#helper code for cleaning up text file 
#only used by newGame()
def removeNewLines(names):
    namesClean =[]
    for x in names:
        x = x.rstrip("\n")
        namesClean.append(x)
    return namesClean

def newGame():
    #get property names from file and put them in name list
    #properties are accessed by their index
    #0 = Go
    #39 = Boardwalk
    inFile = open("Monopoly", "r")
    names = []
    names = inFile.readlines() #returns a list
    inFile.close()
    names = removeNewLines(names)
    
    #intialize list of property visits @ zero
    #properties are accessed by their index
    #0 = Go
    #39 = Boardwalk
    propertyVisits = []
    for x in range(40):
        propertyVisits.append(0)
    
    #intialize player locations @ zero i.e. Go
    playerLocations = []
    for x in range(PLAYERS):
        playerLocations.append(0)
        
    return names, propertyVisits, playerLocations

def displayVisits(propertyVisits, names):
    xCor = names
    yCor = propertyVisits
    plt.figure(figsize=(14,25))
    plt.xticks(size = 10)
    plt.xlabel('Times a Player Landed on Property')
    plt.yticks(size = 10)
    barlist = plt.barh(xCor, yCor, 1)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7)
    barlist[yCor.index(max(yCor))].set_color('yellow')
    plt.show()

def setVisits(propertyVisits, playerLocations):
    for player in range (PLAYERS):
        propertyVisits[playerLocations[player]] +=1 
    return propertyVisits

def roll(doubleCount):
    first = random.randint(1,6)
    second = random.randint(1,6)
    return first + second

def main():
    names, propertyVisits, playerLocations = newGame()
    
    for rounds in range (1000):
        for player in range (PLAYERS):
            playerLocations[player] += roll(0)
            playerLocations[player] = playerLocations[player]%40
            
        propertyVisits = setVisits(propertyVisits, playerLocations)   
    
    displayVisits(propertyVisits, names)







