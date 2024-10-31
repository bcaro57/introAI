import numpy as np
import random

def inputHandler():
    # userInput = input("enter your request. \n")
    userInput = '15 12 8 6 q 11'
    valid = True

    spaceIndexList = [0]
    for index, item in enumerate(userInput):
        if item == ' ':
            spaceIndexList.append(index)
    if userInput[-1] == ' ':
            spaceIndexList.pop(-1)

    inputList = [] 

    if len(spaceIndexList) == 5:
        for space in range(0, 4):
            inputList.append(int(userInput[spaceIndexList[space] : spaceIndexList[space+1]]))
        inputList.append((userInput[spaceIndexList[4]+1 : len(userInput)]))
    
    elif len(spaceIndexList) == 6:
        for space in range(0, 4):
            inputList.append(int(userInput[spaceIndexList[space] : spaceIndexList[space+1]]))
        inputList.append((userInput[spaceIndexList[4]+1 : spaceIndexList[5]]))
        inputList.append(int(userInput[spaceIndexList[5] : len(userInput)]))

    for i, element in enumerate(inputList):
        if (i != 4):
            if element < 0 or element > 16:
                valid = False
                break
        else:
            if element != 'p' and element != 'q':
                valid = False
                break

    if valid:
        
        return inputList
    else:
        print("invalid input. try again. \n\n")
        inputHandler()

def outputHandler(input, board):
    if input[4] == 'p':
        for i in range (1, 17):
            currentPosition = getPosition(i)
            boardInfo = board[currentPosition[0], currentPosition[1]]
            if boardInfo[1] == 0:
                action = chooseAction(boardInfo, ['up','right','down','left'])
                if action == 'up':
                    print(i,'\tup')
                elif action == 'right':
                    print(i,'\tright')
                elif action == 'down':
                    print(i,'\tdown')
                elif action == 'left':
                    print(i,'\tleft')
            elif boardInfo[1] == 1:
                print(i,'\tgoal')
            elif boardInfo[1] == 2:
                print(i,'\tforbid')
            elif boardInfo[1] == 3:
                print(i,'\twall-square')
                
    elif input[4] == 'q':
        currentPosition = getPosition(input[5])
        boardInfo = board[currentPosition[0], currentPosition[1]]
        print('up\t', round(boardInfo[2],2))
        print('right\t', round(boardInfo[3],2))
        print('down\t', round(boardInfo[4],2))
        print('left\t', round(boardInfo[5],2))

def getPosition(value):
    if value%4 == 0:
        row = value//4 - 1
        column = 3
    else:
        row = value//4
        column = value%4 - 1
    return [row, column]

def getIndex(x, y):
    return (x*4 + y) + 1

def setSquareReward(square, reward, special):
    square[0] = reward
    square[1] = special
    return

def setActionSpace(boardInfo):
    if boardInfo[1] == 1 or boardInfo[1] == 2:
        return 'out'
    else:
        return ['up', 'right', 'down', 'left']

def chooseAction(boardInfo, actionList):
    if len(actionList) == 1:
        return 'out'
    else:
        qValues = boardInfo[2:]
        bestQ = -1000
        for i, action in enumerate(['up', 'right', 'down', 'left']):
            if qValues[i] > bestQ:
                bestQ = qValues[i]
                bestAction = action
        return bestAction

def findNextPosition(currentPosition, action, board):
    if action == 'up':
        newPosition = [currentPosition[0]+1, currentPosition[1]]
        if newPosition[0] > 3:
            newPosition[0] = currentPosition[0]
        newBoardInfo = board[newPosition[0], newPosition[1]]
        if newBoardInfo[1] == 3:
            newPosition[0] = currentPosition[0]
        return newPosition
    elif action == 'right':
        newPosition = [currentPosition[0], currentPosition[1]+1]
        if newPosition[1] > 3:
            newPosition[1] = currentPosition[1]
        newBoardInfo = board[newPosition[0], newPosition[1]]
        if newBoardInfo[1] == 3:
            newPosition[1] = currentPosition[1]
        return newPosition
    elif action == 'down':
        newPosition = [currentPosition[0]-1, currentPosition[1]]
        if newPosition[0] < 0:
            newPosition[0] = currentPosition[0]
        newBoardInfo = board[newPosition[0], newPosition[1]]
        if newBoardInfo[1] == 3:
            newPosition[1] = currentPosition[1]
        return newPosition
    elif action == 'left':
        newPosition = [currentPosition[0], currentPosition[1]-1]
        if newPosition[1] < 0:
            newPosition[1] = currentPosition[1]
        newBoardInfo = board[newPosition[0], newPosition[1]]
        if newBoardInfo[1] == 3:
            newPosition[1] = currentPosition[1]
        return newPosition
    else:
        return 0 
    
input = inputHandler()

## each square has 6 values associated with it, depicted as follows:
# 0 :      reward        -  whatever reward should be given when this square is reached
# 1 :       type         -  the type of square it is, where 0 is a normal square, 
#                           1 ia a goal square, 2 is a forbidden square, and 3 is a wall
# 2 :   q value for up   -  self explanitory
# 3 :  q value for right -  self explanitory
# 4 :  q value for down  -  self explanitory
# 5 :  q value for left  -  self explanitory
board = np.zeros((4,4,6), float)

for i in range(1,17):
    x = getPosition(i)
    if i == input[0] or i == input[1]:
        setSquareReward(board[x[0],x[1]], 100, 1)
    elif i == input[2]:
        setSquareReward(board[x[0],x[1]], -100, 2)
    elif i == input[3]:
        setSquareReward(board[x[0],x[1]], -0.1, 3)   
    else:
        setSquareReward(board[x[0],x[1]], -0.1, 0)

gamma = 0.1
alpha = 0.3
epsilon = 0.5
seed = 1
random.seed(seed)
maxIterations = 100000
iteration = 0
currentSquare = 2       # 2 is always the start square

while iteration <= maxIterations:
    # learning loop
    iteration += 1
    currentPosition = getPosition(currentSquare)
    boardInfo = board[currentPosition[0], currentPosition[1]]
    availableActions = setActionSpace(boardInfo)
    # choosing the action
    if len(availableActions) == 1:
        action = availableActions[0]
    elif random.random() < epsilon:
        action = chooseAction(boardInfo, availableActions)
    else:
        action = random.choice(availableActions)
    
    nextPosition = findNextPosition(currentPosition, action, board)
    
    if nextPosition != 0:
        nextSquareInfo = board[nextPosition[0], nextPosition[1]]
        if action == 'up':
            # print((1-alpha)*boardInfo[2] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:])), ', ', action)
            boardInfo[2] = (1-alpha)*boardInfo[2] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:]))
        elif action == 'right':
            # print((1-alpha)*boardInfo[3] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:])), ', ', action)
            boardInfo[3] = (1-alpha)*boardInfo[3] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:]))
        elif action == 'down':
            # print((1-alpha)*boardInfo[4] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:])), ', ', action)
            boardInfo[4] = (1-alpha)*boardInfo[4] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:]))
        elif action == 'left':
            # print((1-alpha)*boardInfo[5] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:])), ', ', action)
            boardInfo[5] = (1-alpha)*boardInfo[5] + alpha*(nextSquareInfo[0] + gamma*max(nextSquareInfo[2:]))
        print(boardInfo[2:], currentSquare)
        currentSquare = getIndex(nextPosition[0], nextPosition[1])

    else:
        currentSquare = 2

outputHandler(input, board)