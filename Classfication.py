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
    for i in len(attribute):
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
    def node(self, trainingDecisions, trainingAttributes):
        entropies = list(map(lambda x: rankAttribute(trainingAttributes, x), trainingAttributes))
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
                for j in len(trainingAttributes)-1:
                    newAttributes.append([])
                #Construct the new list
                for j in len(trainingAttributes[pivotIndex]):
                    if trainingAttributes[pivotIndex][j]==i:
                        for k in len(trainingAttributes):
                            if k!=pivotIndex:
                                newAttributes[k].append(trainingAttributes[pivotIndex][j])
                        newDecision.append(trainingDecisions[j])
                self.children[i] = Node(newDecision, newAttributes)



A1 = [1, 1, 0, 1, 1]
A2 = [0, 0, 1, 1, 1]
A3 = [0, 1, 0, 1, 0]
Y = [False, False, False, True, True]
LA = [A1, A2, A3]
entropies = map(lambda x: rankAttribute(Y, x), LA)
print(list(entropies))
