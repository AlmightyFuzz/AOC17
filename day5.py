test1 = [0,3,0,1,-3]

def jumpJumpJump(maze): #jump up and get down
    jumpNum = 0
    idx = 0

    while True:
        if idx < 0 or idx >= len(maze):
            break

        #extract the jump distance
        jump = maze[idx]

        #update the existing jump value
        if jump >= 3:
            maze[idx] = jump - 1
        else:
            maze[idx] = jump + 1

        #jump to new location
        idx = idx + jump

        #count the jump
        jumpNum += 1

    return jumpNum

def processPuzzleInput():
    data = []
    file = open('day5input.txt', 'r')

    for line in file:
        data.append(int(line))

    print(jumpJumpJump(data))

if __name__ == "__main__":
    print(jumpJumpJump(test1))
    #processPuzzleInput()
