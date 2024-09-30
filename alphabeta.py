class Node:

    def __init__(self, value, a, b, s, i):
        self.v = value
        self.alpha = a
        self.beta = b
        self.state = s
        self.index = i  
    leftKid = None
    middleKid = None
    rightKid = None
    visited = False
    
def value(node):
    if node.state == 'TERMINAL':
        return node.v
    elif node.state == 'MAX':
        return maxValue(node)
    elif node.state == 'MIN':
        return minValue(node)

def maxValue(node):
    for successor in [node.leftKid, node.middleKid, node.rightKid]:
        if successor != None: 
            successor.visited = True
            successor.alpha, successor.beta = node.alpha, node. beta
            node.v = max(node.v, value(successor))
            if node.v >= node.beta:
                return node.v
            node.alpha = max(node.alpha, node.v)
    return node.v

def minValue(node):
    for successor in [node.leftKid, node.middleKid, node.rightKid]:
        if successor != None:    
            successor.visited = True
            successor.alpha, successor.beta = node.alpha, node. beta 
            node.v = min(node.v, value(successor))
            if node.v <= node.alpha:
                return node.v
            node.beta = min(node.beta, node.v)
    return node.v

valid = False
while valid == False:
    userInput = input("enter your number list below\n\n")
    spaceIndexList = [0]
    for index, item in enumerate(userInput):
        if item == ' ':
            spaceIndexList.append(index)
    if userInput[-1] == ' ':
            spaceIndexList.pop(-1)
    
    if (len(spaceIndexList) != 12):
        print("incorrect number of inputs, try again")
    else:
        valid = True

numberList = []
for space in range(0, len(spaceIndexList)-1):
    numberList.append(int(userInput[spaceIndexList[space] : spaceIndexList[space+1]]))
numberList.append(int(userInput[spaceIndexList[-1]+1 : len(userInput)]))

## Setting up the tree

# layer one
root = Node(-1000000000, -1000000000, 1000000000, 'MAX', [0,1,2,3,4,5,6,7,8,9,10,11])
# layer two
root.leftKid = Node(1000000000, -1000000000, 1000000000, 'MIN', [0,1,2,3])
root.middleKid = Node(1000000000, -1000000000, 1000000000, 'MIN', [4,5,6,7])
root.rightKid = Node(1000000000, -1000000000, 1000000000, 'MIN', [8,9,10,11])
# layer three
root.leftKid.leftKid = Node(-1000000000, -1000000000, 1000000000, 'MAX', [0,1])
root.leftKid.rightKid = Node(-1000000000, -1000000000, 1000000000, 'MAX', [2,3])
root.middleKid.leftKid = Node(-1000000000, -1000000000, 1000000000, 'MAX', [4,5])
root.middleKid.rightKid = Node(-1000000000, -1000000000, 1000000000, 'MAX', [6,7])
root.rightKid.leftKid = Node(-1000000000, -1000000000, 1000000000, 'MAX', [8,9])
root.rightKid.rightKid = Node(-1000000000, -1000000000, 1000000000, 'MAX', [10,11])
# layer four - terminal layer
root.leftKid.leftKid.leftKid = Node(numberList[0], -1000000000, 1000000000, 'TERMINAL', 0)
root.leftKid.leftKid.rightKid = Node(numberList[1], -1000000000, 1000000000, 'TERMINAL', 1)
root.leftKid.rightKid.leftKid = Node(numberList[2], -1000000000, 1000000000, 'TERMINAL', 2)
root.leftKid.rightKid.rightKid = Node(numberList[3], -1000000000, 1000000000, 'TERMINAL', 3)
root.middleKid.leftKid.leftKid = Node(numberList[4], -1000000000, 1000000000, 'TERMINAL', 4)
root.middleKid.leftKid.rightKid = Node(numberList[5], -1000000000, 1000000000, 'TERMINAL', 5)
root.middleKid.rightKid.leftKid = Node(numberList[6], -1000000000, 1000000000, 'TERMINAL', 6)
root.middleKid.rightKid.rightKid = Node(numberList[7], -1000000000, 1000000000, 'TERMINAL', 7)
root.rightKid.leftKid.leftKid = Node(numberList[8], -1000000000, 1000000000, 'TERMINAL', 8)
root.rightKid.leftKid.rightKid = Node(numberList[9], -1000000000, 1000000000, 'TERMINAL', 9)
root.rightKid.rightKid.leftKid = Node(numberList[10], -1000000000, 1000000000, 'TERMINAL', 10)
root.rightKid.rightKid.rightKid = Node(numberList[11], -1000000000, 1000000000, 'TERMINAL', 11)

value(root)

indexList = []

if(root.leftKid.leftKid.leftKid.visited == False):
    indexList.append(0)
if(root.leftKid.leftKid.rightKid.visited == False):
    indexList.append(1)
if(root.leftKid.rightKid.leftKid.visited == False):
    indexList.append(2)
if(root.leftKid.rightKid.rightKid.visited == False):
    indexList.append(3)
if(root.middleKid.leftKid.leftKid.visited == False):
    indexList.append(4)
if(root.middleKid.leftKid.rightKid.visited == False):
    indexList.append(5)
if(root.middleKid.rightKid.leftKid.visited == False):
    indexList.append(6)
if(root.middleKid.rightKid.rightKid.visited == False):
    indexList.append(7)
if(root.rightKid.leftKid.leftKid.visited == False):
    indexList.append(8)
if(root.rightKid.leftKid.rightKid.visited == False):
    indexList.append(9)
if(root.rightKid.rightKid.leftKid.visited == False):
    indexList.append(10)
if(root.rightKid.rightKid.rightKid.visited == False):
    indexList.append(11)

print(indexList)