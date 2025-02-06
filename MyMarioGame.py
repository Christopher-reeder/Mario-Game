# MyMarioGame_A5.py
# 
# Description: Mario game has depicted in the sample runs 1, 2 and 3.
#
# Author: Christopher Kade Reeder
# Date: Nov.26 2023


#-------- Assignment 4 section --------

def createMaze(aMaze, aWidth, aHeight, aCell):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "aCell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]
    
    return aMaze

# -------------------------------------------------------------------

# Print Maze - This function is to used for testing and debugging purposes only!
def printMaze(aMaze, aHeight):
    ''' Print "aMaze" of "aHeight" - for testing and debugging purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundaryList(aWidth, bH = "---"):
    ''' Create and return a list that contains 2 lists: the first list
        is the top boundary of the maze and contains a string set to "bH".
        The second list is the bottom boundary of the maze and it also
        contains a string set to "bH".

        Other parameter:
         "aWidth" is the width of the maze.
    '''
    return list([[(bH) for number in range(aWidth)],
                 [(bH) for number in range(aWidth)]])                

# -------------------------------------------------------------------

def displayMaze(aMaze, aWidth, aHeight, hBoundary, bS = "|" ):
    ''' Display "aMaze" with column numbers at the top and row numbers
        to the left of each row along with the top and the bottom boundaries
        "hBoundary" that surround the maze.

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "bS" is the symbol used for the vertical border.
    '''
    
    offset = 3
    aString = (offset+1) * " "

    print()  
    # Display a row of numbers from 1 to aWidth
    for column in range(aWidth):
        aString = aString + str(column+1) + " "
        if len(str(column+1)) == 1 :
            aString += " "           
    print(aString)

    # Display the top boundary of maze
    print(offset * " " + "".join(hBoundary[0])) 
    
    # Display a column of numbers from 1 to aHeight
    # + left and right boundaries of the maze
    for row in range(aHeight):
        pre = str(row+1) + " " + bS

        # If the displayed row number is >= 10 - adjusting for extra digit
        if row >= 9: # Here 9 since we start at 0
           pre = str(row+1) + bS

        post = bS
        aRow = pre + ''.join(aMaze[row]) + post
        print(aRow)

    # Display the bottom boundary of maze
    print(offset * " " + "".join(hBoundary[1]))
    
    return

# -------------------------------------------------------------------

def placeExitGate(aWidth, aHeight, rowMario, columnMario, hBoundary,
                  exitGate = " = "):
    ''' Place the "exitGate" at the opposite corner of Mario's location.
	In other words, place the "exitGate" either in the top boundary or 
	in the bottom boundary whichever is at the opposite corner of
	Mario's location at coordinates ("columnMario","rowMario").

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "hBoundary" is a list of 2 lists: the first list is the top boundary
                                   and the second list is the bottom boundary.

        Returned value:
         "hBoundary" updated.
         "exitGateLocationList" contains coordinates x and y of the "exitgate".
    '''
    
    exitGateRight = False
    exitGateBottom = False

    # Create "exitGateLocationList" with initial location of "exitGate"
    # at the top left of maze
    exitGateLocationList.insert(0, 0)   
    exitGateLocationList.insert(1, 0)
    
    # Where is Mario?
    # If Mario is top left then exit gate is bottom right
    if columnMario <= ((aWidth) // 2) : # Mario on the left?
        exitGateLocationList[1] = aWidth - 1  # Yes, then "exitGate" on right
        exitGateRight = True
    # No, then assuption holds -> exit gate on the left
    if rowMario <= ((aHeight) // 2) :   # Mario at the top?
        exitGateLocationList[0] = aHeight - 1  # Yes, then "exitGate" at bottom
        exitGateBottom = True
        # No, then initial position of "exitGate" holds at the top left of maze

    # Place "exitGate" in appropriate top/bottom boundary
    if exitGateBottom :
        del hBoundary[1][exitGateLocationList[1]]
        hBoundary[1].insert(exitGateLocationList[1], exitGate)
    else:
        del hBoundary[0][exitGateLocationList[1]]
        hBoundary[0].insert(exitGateLocationList[1], exitGate)       

    # Can return a tuple -> elements sepatared by a coma
    return hBoundary, exitGateLocationList  

# -------------------------------------------------------------------


# ***Main part of the program

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
# filename = input("Please, enter a filename: ")

# Open file for reading
filename = 'InputData.txt'
openFile = open(filename, "r") 

# Read the content of the file, one line at a time, and and initialize 
# the following variables in the order these variables are listed
# mazeWidth, mazeHeight, aNumOfTreasures, aNumOfBombs must be assigned
# an integer value

# variable that show the number of the line
line = 0

for i in openFile:

    if line == 0: 
        mazeWidth = int(i) 

    elif line == 1:
        mazeHeight = int(i) 

    elif line == 2:
        aNumOfTreasures = int(i) 

    elif line == 3:
        aNumOfBombs = int(i) 

# emptyCell, obstacle, mario must be assigned a string

    elif line == 4:
        emptyCell = i[:3] 

    elif line == 5:
        obstacle = i[:3] 

    elif line == 6:
        mario = i[:3]

# marioLocationList must contain a list with two elements
# (of type "str") representing the coordinates x and y of Mario's
# location in the maze. For example: ['0', '0']

    elif line == 7:
        
        marioLocationList = [i[0], i[2]]

# obstacleLocationDict must be a dictionary with items formatted as
# follows: {(x,y): -1} if there is a bomb in the cell at location x,y 
# in the maze and {(x,y): 1} if there is a treasure at the location x,y
# in the maze. If the cell is empty at the location x,y in the maze,
# this location is not stored in the dictionary obstacleLocationDict

        obstacleLocationDict = {}

    elif 8 <= line <= 22:
        
        key = (str(i[0]), str(i[2]))
        value = 1
        obstacleLocationDict[key] = value

    elif 23 <= line <= 52:

        key = (str(i[0]), str(i[2]))
        value = -1
        obstacleLocationDict[key] = value

# bombScoreRatio must be assigned an integer value

    elif line == 53:
        
        bombScoreRatio = int(i)

    line += 1


# Close the file
openFile.close()

# Create a maze
theMaze = list()
theMaze = createMaze(theMaze, mazeWidth, mazeHeight, emptyCell)

# Create the top and bottom boundaries of the maze
# These boundaries are not part of the maze
hBoundary = list()
hBoundary = createBoundaryList(mazeWidth)

# Place the character (string) "obstacle" in the maze
# This is how we hide the treasures and bombs from the player
for i in obstacleLocationDict:
    if obstacleLocationDict[i] == 1 or obstacleLocationDict[i] == -1:
        theMaze[int(i[0])][int(i[1])] = obstacle

# Place Mario in the maze
theMaze[int(marioLocationList[0])][int(marioLocationList[1])] = mario

         
# Call the appropriate function which computes the location of the
# exit gate and places it in either the top or the bottom boundary
exitGateLocationList = list()
placeExitGate(mazeWidth, mazeHeight, int(marioLocationList[0]),\
              int(marioLocationList[1]), hBoundary)

# Call the appropriate function to display the maze 
displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary)



print("\n-------")


#------ Assignment 5 starts here ------
      
# Set Mario's score - Done!
# Setting Marios's score has already been done for you
# so you do not have to add any code to the following line:
marioScore = aNumOfBombs // bombScoreRatio

#--- The Algorithm for Assignment 5 starts here ---

# This is the algorithm of the game engine, expressed as comments.
# Your task is to convert these comments into corresponding Python code.

# Set the condition variables for your loop
playing = True

# As long as the player is playing AND marioScore > 0 AND
# Mario has not reached the exit gate, loop i.e., play:
while playing and marioScore > 0 and marioLocationList != exitGateLocationList:

    # Display the maze
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary)

    # Display Mario's score (see Sample Runs)
    print(f"\nMario's score: {marioScore}")
  
    # Display instructions to the player (see Sample Runs)
    print("\nMove Right:'r', Move Left:'l', Move Up:'u', Move Down:'d', Exit:'x'")
    
    # Ask the player (user) to enter either 'r' for right, 'l' for left,
    move = input("Your move: ")
    
    # Error check: if nothing or anything else is entered,
    while move not in ['r', 'l', 'u', 'd', 'x']:
        print("Invalid move. Please try again.")
        # just reprint the prompt to player.
        move = input("Your move: ")

    # If the player is moving Mario one cell to the right
        # Update Mario's location (hint: create a new marioNewLocationList)
        # If Mario new location is still within the maze, i.e.,
        # Mario has no hit the right boundary of the maze then
            # Erase Mario from his current location in the maze.
            # Move Mario to his new location in the maze.
            
            # Check whether Mario has stepped onto an obstacle and if so,
            # update Mario's score.
            # Finally, print appropriate win/lost statement if the player
            # has won/lost the game.
            # Make sure you update Mario's current location to be his new location.
    if move == 'r':
        if int(marioLocationList[1])+1 < mazeWidth:
            theMaze[int(marioLocationList[0])][int(marioLocationList[1])+1] = mario
            theMaze[int(marioLocationList[0])][int(marioLocationList[1])] = emptyCell
            marioLocationList[1] = str(int(marioLocationList[1])+1)
            
            if tuple(marioLocationList) in obstacleLocationDict:
                obstacleType = obstacleLocationDict[tuple(marioLocationList)]
                marioScore += obstacleType
                if obstacleType == 1:
                    print("Congratulations! You found a treasure.")
                elif obstacleType == -1:
                    print("Oops! Mario stepped on a bomb.")
                
    # If the player is moving Mario one cell to the left
        # Update Mario's location (hint: create a new marioNewLocationList)
        # If Mario new location is still within the maze, i.e.,
        # Mario has no hit the left boundary of the maze then
            # Erase Mario from his current location in the maze.
            # Move Mario to his new location in the maze.
            # Check whether Mario has stepped onto an obstacle and if so,
            # update Mario's score.
            # Finally, print appropriate win/lost statement if the player
            # has won/lost the game.
            # Make sure you update Mario's current location to be his new location.
    elif move == 'l':
        if -1 < int(marioLocationList[1])-1 < mazeWidth:
            theMaze[int(marioLocationList[0])][int(marioLocationList[1])-1] = mario
            theMaze[int(marioLocationList[0])][int(marioLocationList[1])] = emptyCell
            marioLocationList[1] = str(int(marioLocationList[1])-1)
            
            if tuple(marioLocationList) in obstacleLocationDict:
                obstacleType = obstacleLocationDict[tuple(marioLocationList)]
                marioScore += obstacleType
                if obstacleType == 1:
                    print("Congratulations! You found a treasure.")
                elif obstacleType == -1:
                    print("Oops! Mario stepped on a bomb.")

    # If the player is moving Mario one cell up
        # Update Mario's location (hint: create a new marioNewLocationList)
        # Has Mario reached the exit gate?
            # Print appropriate win/lost statement if the player
            # has won/lost the game.
        # Otherwise
            # Erase Mario from his current location in the maze.
            # Move Mario to his new location in the maze.
            # Check whether Mario has stepped onto an obstacle and if so,
            # update Mario's score.
            # Finally, print appropriate win/lost statement if the player
            # has won/lost the game.
            # Make sure you update Mario's current location to be his new location.
    elif move == 'u':
        
        if int(marioLocationList[0]) == int(exitGateLocationList[0])\
           and int(marioLocationList[1]) == int(exitGateLocationList[1]):
            print("Congratulations! You reached the exit gate.")
            playing = False
            break
        
        if -1 < int(marioLocationList[0])-1 <= mazeHeight:
            theMaze[int(marioLocationList[0])-1][int(marioLocationList[1])] = mario
            theMaze[int(marioLocationList[0])][int(marioLocationList[1])] = emptyCell
            marioLocationList[0] = str(int(marioLocationList[0])-1)
            
            if tuple(marioLocationList) in obstacleLocationDict:
                obstacleType = obstacleLocationDict[tuple(marioLocationList)]
                marioScore += obstacleType
                if obstacleType == 1:
                    print("Congratulations! You found a treasure.")
                elif obstacleType == -1:
                    print("Oops! Mario stepped on a bomb.")
        
    # If the player is moving Mario one cell down
        # Update Mario's location (hint: create a new marioNewLocationList)
        # Has Mario reached the exit gate?
        # Why do we need to check this since the exit gate is located at the top?
        # Answer: Remember, the exit gate could have been placed in the bottom
        #  boundary if Mario had initially been located in the top part of the maze.
            # Print appropriate win/lost statement if the player
            # has won/lost the game.
        # Otherwise
            # Erase Mario from his current location in the maze.
            # Move Mario to his new location in the maze.
            # Check whether Mario has stepped onto an obstacle and if so,
            # update Mario's score.
            # Finally, print appropriate win/lost statement if the player
            # has won/lost the game.
            # Make sure you update Mario's current location to be his new location.  
    elif move == 'd':
                
        if int(marioLocationList[0]) == int(exitGateLocationList[0])\
           and int(marioLocationList[1]) == int(exitGateLocationList[1]):
            print("Congratulations! You reached the exit gate.")
            playing = False
            break
        
        if int(marioLocationList[0])+1 < mazeHeight:
            theMaze[int(marioLocationList[0])+1][int(marioLocationList[1])] = mario
            theMaze[int(marioLocationList[0])][int(marioLocationList[1])] = emptyCell
            marioLocationList[0] = str(int(marioLocationList[0])+1)
            
            if tuple(marioLocationList) in obstacleLocationDict:
                obstacleType = obstacleLocationDict[tuple(marioLocationList)]
                marioScore += obstacleType
                if obstacleType == 1:
                    print("Congratulations! You found a treasure.")
                elif obstacleType == -1:
                    print("Oops! Mario stepped on a bomb.")
    
    # If the player has entered 'x', then stop the game.
    elif move == 'x':
        playing = False           

# End of the game
print("\nBye!")
print("\n-------!")

