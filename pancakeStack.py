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

def heuristic(state):
    stateList = list(state)
    if stateList[6] == '4':
        if stateList[4] == '3':
            if stateList[2] == '2':
                if stateList[0] == '1':
                    if stateList[1] == 'b':
                        return 0
                    else:
                        return 0
            else:
                return 2
        else:
            return 3
    else:
        return 4
    
def costCalculator(flipOrderList):
    flipList = []
    costList = []
    for flip in flipOrderList:
        flipList.append(int(flip))
        costList.append(str(sum(flipList)))

    return costList

# not started
def aStarSearch(userInput):
    stateSpace = []
    costSpace = []
    hasSeenList = []
    currentState = userInput[0:8] + '-'
    stateSpace.append(currentState)
    costSpace.append(0)

    while stateSpace:
        # identify the lowest cost, look for ties 
        #
        # if there are no ties, it will consider the one value by itself and look for the max of 1 element... 
        # kinda stupid but i dont mind it too much since it seems to work

        val = min(costSpace)
        tieList = []
        tieNumberList = []
        tieIndexList = []
        for index, number in enumerate(costSpace):
            val = number + heuristic(stateSpace[index][0:8])
            if len(tieNumberList) == 0:
                tieNumberList.append(stateSpace[index][0:8])
                tieIndexList.append(index)
            
            if val < costSpace[tieIndexList[0]] + heuristic(tieNumberList[0]):
                tieNumberList = []
                tieIndexList = []
                tieNumberList.append(stateSpace[index][0:8])
                tieIndexList.append(index)
            elif val == costSpace[tieIndexList[0]] + heuristic(tieNumberList[0]):
                if len(tieNumberList) != 1:
                    tieNumberList.append(stateSpace[index][0:8])
                    tieIndexList.append(index)
        tieList.append(tieNumberList)
        tieList.append(tieIndexList)
        
        # turn the tied items into numbers
        for tieIndex, ties in enumerate(tieList[0]):
            tieItem = list(ties)
            for i in range(1,8,2):
                if (tieItem[i] == 'b'):
                    tieItem[i] = '0'
                elif (tieItem[i] == 'w'):
                    tieItem[i] = '1'
            tieList[0][tieIndex] = ''.join(tieItem)

        # handle the ties and determines the item we will use
        maxTie = max(tieList[0])
        currentIndex = tieList[1][tieList[0].index(maxTie)]
        currentState = stateSpace[currentIndex]

        for flipLayer in range(1,5,1):

            currentStateList = list(currentState)
            currentStateList[0:8] = flip(stateSpace[currentIndex][0:8], flipLayer)
            currentState = ''.join(currentStateList)
            
            if currentState[0:8] == '1w2w3w4w':
                return stateSpace[currentIndex][9:len(currentState)+1] + str(flipLayer)

            if currentState[0:8] not in hasSeenList:
                hasSeenList.append(currentState[0:8])
                stateSpace.append(currentState + str(flipLayer))
                costSpace.append(flipLayer + costSpace[currentIndex])

        stateSpace.pop(currentIndex)
        costSpace.pop(currentIndex)


# prints the A* result in the proper format
def printAStarSearchResult(startState, order):
    currentState = startState
    orderList  = list(order)
    costList = costCalculator(orderList)

    orderList.append('0')
    costList.insert(0, '0')

    while(len(orderList) > 0):
        if(orderList[0] == '1'):
            print(currentState[0:2] + '|' + currentState[2:8] + ' g:' + costList[0] + ' h: ' + str(heuristic(currentState[0:8])))
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '2'):
            print(currentState[0:4] + '|' + currentState[4:8] + ' g:' + costList[0] + ' h: ' + str(heuristic(currentState[0:8])))
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '3'):
            print(currentState[0:6] + '|' + currentState[6:8] + ' g:' + costList[0] + ' h: ' + str(heuristic(currentState[0:8])))
            currentState = flip(currentState, int(orderList[0]))
        elif(orderList[0] == '4'):
            print(currentState[0:8] + '|' + ' g:' + costList[0] + ' h: ' + str(heuristic(currentState[0:8])))
            currentState = flip(currentState, int(orderList[0]))
        else:
            print(currentState + ' g:' + costList[0] + ' h: 0')
        orderList.pop(0)
        costList.pop(0)
    return

# this function uses a BFS algorithm to sort through the stack
def breadthForSearch(userInput):
    stateSpace = []
    currentState = userInput[0:8] + '-'
    stateSpace.append(currentState)

    while currentState[0:8] != '1w2w3w4w':
        currentState = stateSpace[0]
        for flipLayer in range(1,5,1):
            currentStateList = list(currentState)
            currentStateList[0:8] = flip(stateSpace[0][0:8], flipLayer)
            currentState = ''.join(currentStateList)

            stateSpace.append(currentState + str(flipLayer))

            if currentState[0:8] == '1w2w3w4w':
                currentState = currentState + str(flipLayer)
                return currentState[9:len(currentState)+1]

        stateSpace.pop(0)
    return currentState[9:len(currentState)+1]

# prints the BFS result in the proper format
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
    printAStarSearchResult(userInput[0:8], aStarSearch(userInput))
elif(userInput[9] == 'b'):
    print('\ni see that you have challenged my BFS search algorithm... \n\n\n                   BEHOLD!\n')
    printBreadthForSearchResult(userInput[0:8], breadthForSearch(userInput))
