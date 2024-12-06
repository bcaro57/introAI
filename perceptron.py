import numpy as np

def inputHandler():
    userInput = input("enter your request. \n")
    userInput = userInput.split(' (')

    functionType = userInput[0]
    triplets = userInput[1:]
    tripletList = []

    for triplet in triplets:
        triplet = triplet.strip(')')
        triplet = triplet.split(',')
        triplet = [float(triplet[0]), float(triplet[1]), float(triplet[2])]
        tripletList.append(triplet)

    return functionType, tripletList

def runPerceptron(tripletList):
    w = [0,0]

    for i in range(0, 100):
        for triplet in tripletList:
            x1 = triplet[0]
            x2 = triplet[1]
            y = triplet[2]

            yHat = w[0]*x1 + w[1]*x2

            if yHat >= 0.0:
                yHat = 1.0
            else:
                yHat = -1.0
            
            if yHat != y:
                w[0] = w[0] + y*x1
                w[1] = w[1] + y*x2
    return w

def runLogisticRegression(tripletList):
    alpha = 0.1
    w = [0,0]
    probabilityList = []

    for i in range(0, 100):
        for triplet in tripletList:
            x1 = triplet[0]
            x2 = triplet[1]
            y = triplet[2]

            if y == -1:
                y = 0
            
            z = w[0]*x1 + w[1]*x2
            g = 1.0 / (1.0 + np.exp(-z))
            w[0] = w[0] + alpha*(y-g)*x1
            w[1] = w[1] + alpha*(y-g)*x2
    
    for triplet in tripletList:
        x1 = triplet[0]
        x2 = triplet[1]
        y = triplet[2]
        z = w[0]*x1 + w[1]*x2
        g = 1.0 / (1.0 + np.exp(-z))

        probabilityList.append(round(g, 2))

    return probabilityList

finished = False

while finished == False:
    fType, tList = inputHandler()

    if fType == 'P':
        w = runPerceptron(tList)
        print(str(w[0]) + ', ' + str(w[1]))

        finished = True
    elif fType == 'L':
        probList = runLogisticRegression(tList)
        delimiter = ' '
        probStr = map(str, probList)
        print(delimiter.join(probStr))
        finished = True
    else:
        print('invalid input, please retry.\n')
        finished = False