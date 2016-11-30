from math import log


def calcEntropy(sortedAttribute):
    positives = sortedAttribute.count(1)
    negatives = len(sortedAttribute)-positives
    q = positives/(positives+negatives)
    return -q * log(q,2) - (1-q) * log(1-q,2)


def rankAttribute(decisions, attribute):
    entropy = None
    positiveYs = []
    negativeYs = []
    for i in range(len(attribute)):
        if attribute[i] == 1:
            positiveYs.append(decisions[i])
        else:
            negativeYs.append(decisions[i])
    if len(positiveYs)==len(attribute) or len(negativeYs)==len(attribute):
        entropy = 0
    else:
        ys = (positiveYs, negativeYs)
        entropy = sum(map(lambda x: len(x) + calcEntropy(x)), ys)
    return entropy




class Node:
    isLeaf = None
    children = {}
    def __init__(self, trainingDecisions, trainingAttributes):
        entropies = list(map(lambda x: rankAttribute(trainingDecisions, x), trainingAttributes))
        #Check if they are all homogenous sets
        if all(map(lambda x: x==0, entropies)):
            #We are a leaf
            self.isLeaf = True
        else:
            self.isLeaf = False
            pivotIndex = entropies.index(max(entropies))
            vals = (1,0)
            for i in vals:
                newDecision = []
                newAttributes = []
                for j in range(len(trainingAttributes)-1):
                    newAttributes.append([])
                #Construct the new list
                for j in range(len(trainingAttributes[pivotIndex])):
                    if trainingAttributes[pivotIndex][j]==i:
                        for k in range(len(trainingAttributes)):
                            if k!=pivotIndex:
                                newAttributes[k].append(trainingAttributes[pivotIndex][j])
                        newDecision.append(trainingDecisions[j])
                self.children[i] = Node(newDecision, newAttributes)



A1 = [1,1,1,1,1,]
A2 = [1, 1, 0, 1, 1]
A3 = [0, 0, 1, 1, 1]
A4 = [0, 1, 0, 1, 0]
Y = [0,0,0,1,1]
LA = [A1, A2, A3, A4]
topNode = Node(Y, LA)
