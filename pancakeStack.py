## flips the pancake stack depending on which layer you decide to make your flip 
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
        stateList[0:2] = stateList[0:2]
        state = ''.join(stateList)
    elif (layer == 2):
        stateList = list(state)
        stateList[0:2], stateList[2:4] = stateList[2:4], stateList[0:2]
        state = ''.join(stateList)
    elif (layer == 3):
        stateList = list(state)
        stateList[0:2], stateList[2:4], stateList[4:6] = stateList[4:6], stateList[2:4], stateList[0:2]
        state = ''.join(stateList)
    elif (layer == 4):
        stateList = list(state)
        stateList[0:2], stateList[2:4], stateList[4:6], stateList[6:8] = stateList[6:8], stateList[4:6], stateList[2:4], stateList[0:2]
        state = ''.join(stateList)
    return state
## not started
def aStarSearch(userInput):
    stateSpace = []
    currentState = userInput[0:8] + "-0-"
    stateSpace.append(currentState)

    while currentState[0:8] != '1w2w3w4w':
        return

    return currentState[9:len(currentState)+1]

## prints the A* result in the proper format
def printAStarSearchResult(startState, order):
    currentState = startState
    orderList = list(order)
    while(len(orderList) > 0):
        if(orderList[0] == '1'):
            print(currentState[0:2] + '|' + currentState[2:8] + ' g:' + currentState[9] + ' h: 1')
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '2'):
            print(currentState[0:4] + '|' + currentState[4:8] + ' g:' + currentState[9] + ' h: 2')
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '3'):
            print(currentState[0:6] + '|' + currentState[6:8] + ' g:' + currentState[9] + ' h: 3')
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '4'):
            print(currentState[0:8] + '|' + ' g:' + currentState[9] + ' h: 4')
            currentState = flip(currentState, int(orderList[0]))
        orderList.pop(0)
    print(currentState)
    return

def breadthForSearch(userInput):
    stateSpace = []
    currentState = userInput[0:8] + "-"
    stateSpace.append(currentState)

    while currentState[0:8] != '1w2w3w4w':
        currentState = stateSpace[0]
        for i in range(1,5,1):
            currentStateList = list(currentState)
            currentStateList[0:8] = flip(stateSpace[0][0:8], i)
            currentState = ''.join(currentStateList)

            stateSpace.append(currentState + str(i))

            if currentState[0:8] == '1w2w3w4w':
                currentState = currentState + str(i)
                return currentState[9:len(currentState)+1]

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


userInput = input('welcome pancake challenger. enter your challenge, if you dare... \n\n')



valid = False

while valid == False:
    userInputList = list(userInput)
    hasSeen = set()
    for number in range(0, len(userInput), 2):
        if userInput[number] in hasSeen:
            hasRepeatNumbers = True
        hasSeen.add(userInput[number])
    hasRepeatNumbers = False

    if (len(userInput) == 10) and all(0 < int(userInputList[i]) < 5 for i in [0, 2, 4, 6]) and hasRepeatNumbers == False and all(userInputList[i] in ['b', 'w'] for i in [1, 3, 5, 7]) and userInputList[9] in ['a', 'b']:
        valid = True
    else:
        print('foolish challenger... your request is dishonorable. what are you, scared?')
        userInput = input('give me a REAL challenge!\n\n')


if(userInput[9] == 'a'):
    print('\ni see that you have challenged my A* search algorithm... \n\n\n                    BEHOLD!\n')
    print(aStarSearch(userInput))
elif(userInput[9] == 'b'):
    print('\ni see that you have challenged my BFS search algorithm... \n\n\n                   BEHOLD!\n')
    printBreadthForSearchResult(userInput[0:8], breadthForSearch(userInput))
