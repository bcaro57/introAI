## flips the pancake stack depending on which layer you decide to make your flip 
def flip(state, layer):
    # changing the orientation
    for n in range(1, 2*layer, 2):
        if (state[n] == 'b'):
            state[n] = 'w'
        elif (state[n] == 'w'):
            state[n] = 'b'
    
    # changing the pancake order
    if (layer == 1):
        state[0] = state[0]
    elif (layer == 2):
        state[0], state[2] = state[2], state[0]
    elif (layer == 3):
        state[0], state[2], state[4] = state[4], state[2], state[0]
    elif (layer == 4):
        state[0], state[2], state[4], state[6] = state[6], state[4], state[2], state[0]
    return state

## not started
def aStarSearch(userInput):
    stateSpace = []
    currentState = userInput[0:8]
    currentState = userInput[0:8] + "-0-"
    stateSpace.append(currentState)

    return currentState[9:len(currentState)+1]

## not started
def printAStarResult():
    return

## uses BFS search algorithm to find which layers need to be flipped, returns a list 
# of numbers that corresponds to which layers get flipped, starting at the leftmost entry
def breadthForSearch(userInput):
    stateSpace = []
    currentState = [userInput[0:8], '']
    stateSpace.append(currentState)
    if ''.join(currentState[0]) == '1w2w3w4w':
        return '0'

    while ''.join(currentState[0]) != '1w2w3w4w':
        currentState = stateSpace[0]
        for i in range(1,5,1):
            currentState[0] = flip(stateSpace[0][0], i)
            currentState[1] = stateSpace[0][1] + str(i)
            stateSpace.append(currentState)

            if ''.join(currentState[0]) == '1w2w3w4w':
                currentState[1]  = currentState[1] + str(i)
                break
        stateSpace.pop(0)
    return currentState[9:len(currentState)+1]

## prints the BFS result in the proper format
def printBreadthForSearchResult(startState, order):
    currentState = startState
    orderList = list(order)
    while(len(orderList) > 0):
        if(orderList[0] == '1'):
            print(currentState[0:2] + '|' + currentState[2:8])
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '2'):
            print(currentState[0:4] + '|' + currentState[4:8])
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '3'):
            print(currentState[0:6] + '|' + currentState[6:8])
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '4'):
            print(currentState[0:8] + '|')
            currentState = flip(currentState, int(orderList[0]))
        orderList.pop(0)
    print(currentState)
    return

userInput = list(input('welcome pancake challenger. enter your challenge, if you dare... \n\n'))

if(userInput[9] == 'a'):
    print('\ni see that you have challenged my A* search algorithm... \n\n\n                    BEHOLD!\n')
    print(aStarSearch(userInput))
elif(userInput[9] == 'b'):
    print('\ni see that you have challenged my BFS search algorithm... \n\n\n                   BEHOLD!\n')
    printBreadthForSearchResult(userInput[0:8], breadthForSearch(userInput))
else:
    print('foolish challenger... your request is dishonorable. what are you, scared?')
    input('give me a REAL challenge!\n\n')
    userInput = list(input('welcome pancake challenger. enter your challenge, if you dare... \n\n'))