from math import log


def calcEntropy(positives, negatives):
    if positives==0 or negatives==0:
        return 0
    q = positives/(positives+negatives)
    return -q * log(q,2) - (1-q) * log(1-q,2)


def rankAttribute(decisions, attribute):
    positives =


class node:
    isLeaf = None
    def node(self, trainingDecisions, trainingAttributes):
        entropies = map(lambda x: rankAttribute(trainingAttributes, x), trainingAttributes)
        #Check if they are all homogenous sets



A1 = [1, 1, 0, 1, 1]
A2 = [0, 0, 1, 1, 1]
A3 = [0, 1, 0, 1, 0]
Y = [False, False, False, True, True]
LA = [A1, A2, A3]
entropies = map(lambda x: rankAttribute(Y, x), LA)
print(list(entropies))
