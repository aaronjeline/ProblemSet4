from math import log


def calcEntropy(sortedAttribute):
    positives = sortedAttribute.count(1)
    negatives = len(sortedAttribute)-positives
    if positives==0 or negatives==0:
        return 0
    q = positives/(positives+negatives)
    return -q * log(q,2) - (1-q) * log(1-q,2)


def rankAttribute(decisions, attribute):
    results = ([],[])
    vals = (0,1)
    for i in range(len(attribute)):
        results[attribute[i]].append(decisions[i])
    weightedSum = sum(map(lambda x: len(x) * calcEntropy(x), results))
    return weightedSum



class Node:
    isLeaf = None
    children = {}
    answer = None
    pivotIndex = None
    def __init__(self, trainingDecisions, trainingAttributes, isLeaf=False):
        self.isLeaf = isLeaf
        if isLeaf:
            self.answer = trainingDecisions[0]
            self.children = None
            print("Leaf! answer = " + str(self.answer))
            return
        entropies = list(map(lambda x: rankAttribute(trainingDecisions, x), trainingAttributes))
        #Pick the best attribute to work with
        pivotIndex = entropies.index(min(entropies))

        vals = (1,0)
        for i in vals:
            newDecision = []
            newAttributes = []
            for j in range(len(trainingAttributes)):
                newAttributes.append([])
            #Construct the new list
            for j in range(len(trainingAttributes[pivotIndex])):
                if trainingAttributes[pivotIndex][j]==i:
                    for k in range(len(trainingAttributes)):
                            newAttributes[k].append(trainingAttributes[k][j])
                    newDecision.append(trainingDecisions[j])
            newAttributes.pop(pivotIndex)
            _isLeaf = None
            if all(map(lambda x: x==0, newDecision)) or all(map(lambda x: x==1, newDecision)):
                #Our child is a leaf!
                _isLeaf = True
            else:
                _isLeaf = False
                self.pivotIndex = pivotIndex

            #Create the new child
            print("Branch! Attribute "+ str(pivotIndex) + "val: " + str(i))
            self.children[i] = Node(newDecision, newAttributes, _isLeaf)




A1 = [1, 1, 0, 1, 1]
A2 = [0, 0, 1, 1, 1]
A3 = [0, 1, 0, 1, 0]
Y = [0,0,0,1,1]
LA = [A1, A2, A3]
topNode = Node(Y, LA)
