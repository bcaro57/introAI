def value(state, alpha, beta):
    if state in numberList:
        nextAgent = 'MAX'
    if nextAgent == 'MAX':
        return maxValue(state, alpha, beta)
    elif nextAgent == 'MIN':
        return minValue(state, alpha, beta)

def maxValue(state, alpha, beta):
    v = -1000000000
    for successor in state:
        v = max(v,value(successor, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValue(state, alpha, beta):
    v = 1000000000  
    for successor in state:
        v = min(v,value(successor, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def pruner(numberList):
    for number in numberList:
        return

valid = False
while valid == False:
    userInput = input("enter your number list below\n\n")
    spaceIndexList = [0]
    for index, item in enumerate(userInput):
        if item == ' ':
            spaceIndexList.append(index)
    if userInput[-1] == ' ':
            spaceIndexList.pop(-1)
    
    if (len(spaceIndexList) != 3):
        print("incorrect number of inputs, try again")
    else:
        valid = True

numberList = []
for space in range(0, len(spaceIndexList)-1):
    numberList.append(int(userInput[spaceIndexList[space] : spaceIndexList[space+1]]))
numberList.append(int(userInput[spaceIndexList[-1]+1 : len(userInput)]))

