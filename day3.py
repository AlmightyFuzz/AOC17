from enum import Enum, auto

puzzleInput = 325489
test1 = 1    #0
test2 = 12   #3
test3 = 23   #2
test4 = 1024 #31

# The program works by keeping track of the current position in the spiral
# memory sequence as a 2D point relative to the start point, and also keeps
# track of the direction of travel and at which values to change direction.
# It then just steps through the until it reaches the destination valuem,
# at which point it uses its 2D point to work out the distance back to the start

def SpiralMemory(targetNum):
    #Start at value of 1, represented as (0,0), with starting direction being East
    direc = Direction.South
    point = Point(0,0)
    count = 1
    cellValue = 0

    spiralData = {str(point): 1}
    #str(Point(xVal,yVal)) converts the point to the string '[xVal,yVal]'
    #spiralData[str(Point(0,0))] = 3

    #Initialise the first turning number    
    turningNumGen = getNextTurningNum()
    turningNum = next(turningNumGen)

    while count <= targetNum:

        if count == 1:
            point.X, point.Y = 0, 0
        else:
            if direc == Direction.East:
                point.X += 1
            elif direc == Direction.North:
                point.Y += 1
            elif direc == Direction.West:
                point.X -= 1
            elif direc == Direction.South:
                point.Y -= 1

        if count == turningNum:
            direc = changeDirection(direc)
            turningNum = next(turningNumGen)

        #cellValue = findCellValue(point,spiralData)

        #spiralData[str(point)] = cellValue

        count += 1

    steps = abs(point.X) + abs(point.Y)

    return steps

#Check the 8 adjacent cells for their values. If there is no value for that cell
#then just carry on to the next. So long as this done for each cell as you work
#your way around the spiral then it should find the correct values, as the blank
#adjacent cells are just ones we haven't reached yet and therefore dont care about
def findCellValue(point, spiralData):
    cellValue = 0
    pX, pY = point.X, point.Y

    #print(pX,pY)
    otherPoint = Point(point.X,point.Y)

    

    return cellValue

# Returns the next direction to travel in depending on the direction given to it
# ie. anti-clockwise
def changeDirection(direction):
    if direction == Direction.North:
        return Direction.West
    elif direction == Direction.West:
        return Direction.South
    elif direction == Direction.South:
        return Direction.East
    elif direction == Direction.East:
        return Direction.North

# The 'turning numbers' (ie, where the direction of travel changes)
# are 1,2,3,5,7,10,13,17,etc.
# The differnce betweeen the those numbers
# are 1,1,2,2,3,3,4,etc.
def getNextTurningNum():
    nextNum = 1
    gen = generator()

    while True:
        yield nextNum

        nextNum += next(gen)

# Generates the sequence 1,1,2,2,3,3,4,4,5,5 etc
def generator():
    num = 1
    flipFlop = False

    while True:
        yield num

        if flipFlop == True:
            num += 1
            flipFlop = False
        else:
            flipFlop = True

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "[{0},{1}]".format(self.X,self.Y)

class Direction(Enum):
    #Note auto() requires Python 3.6+
    North = auto()
    East = auto()
    South = auto()
    West = auto()

if __name__ == '__main__':    
    #print(SpiralMemory(test1)) #0
    print(SpiralMemory(test2)) #3
    #print(SpiralMemory(test3)) #2
    #print(SpiralMemory(test4)) #31

    #print(SpiralMemory(puzzleInput))
