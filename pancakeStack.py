def flip(state, layer):
    # changing the orientation
    for n in range(1, 2*layer, 2):
        stateList = list(state)
        if (state[n] == 'b'):
            stateList[n] = 'w'
        elif (state[n] == 'w'):
            stateList[n] = 'b'
        state = ''.join(stateList)
    
    # changing the pancake order
    if (layer == 1):
        stateList = list(state)
        stateList[0] = stateList[0]
        state = ''.join(stateList)
    elif (layer == 2):
        stateList = list(state)
        stateList[0], stateList[2] = stateList[2], stateList[0]
        state = ''.join(stateList)
    elif (layer == 3):
        stateList = list(state)
        stateList[0], stateList[2], stateList[4] = stateList[4], stateList[2], stateList[0]
        state = ''.join(stateList)
    elif (layer == 4):
        stateList = list(state)
        stateList[0], stateList[2], stateList[4], stateList[6] = stateList[6], stateList[4], stateList[2], stateList[0]
        state = ''.join(stateList)
    return state

# not started
def aStarSearch(userInput):
    currentState = userInput[0:8]
    return currentState

# started, but not finished
def breadthForSearch(userInput):
    stateSpace = []
    currentState = userInput[0:8]
    stateSpace.append(currentState)
    while currentState != '1w2w3w4w':
        for i in range(1,5,1):
            currentState = flip(stateSpace[0], i)
            stateSpace.append(currentState)
        stateSpace.pop(0)
    return stateSpace

print(breadthForSearch('1b2w3b4w'))
# userInput = input('welcome pancake challenger. enter your challenge, if you dare... \n\n')

# if(userInput[9] == 'a'):
#     print('\ni see that you have challenged my A* search algorithm... \n\n\n                    BEHOLD!\n')
#     print(aStarSearch(userInput))
# elif(userInput[9] == 'b'):
#     print('\ni see that you have challenged my BFS search algorithm... \n\n\n                   BEHOLD!\n')
#     print(breadthForSearch(userInput))
# else:
#     print('foolish challenger... your request is dishonorable. what are you, scared?')
#     input('give me a REAL challenge!\n\n')