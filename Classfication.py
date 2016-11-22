from math import log
def calcEntropy(positives, negatives):
    if positives==0 or negatives==0:
        return 0
    q = positives/(positives+negatives)
    return -q * log(q,2) - (1-q) * log(1-q,2)

def calcEntropy(decisions, attribute):
    uniques, results = [], []
    for val in attribute:
        if val not in uniques:
            uniques.add(val)
    for val in uniques:
        positives, negatives = 0, 0
        for i in range(len(attribute)-1):
            if val == attribute[i]:
                if decisions[i]:
                    positives += 1
                else:
                    negatives += 1
        sum = positives + negatives
        entropy = calcEntropy(positives, negatives)
        results.append((sum, entropy))
    totalSum = sum(map(lambda x: x[1], results))
    weightedAverage = sum(map(lambda x: x[0]*x[1], results))/totalSum
    return (weightedAverage, uniques)


#decisions is a list of booleans, attributes is a list of lists containing attributes
def classify(decisions, attributes, name):
    #Check to make sure all the sizing works out
    assert(all(map(lambda x:len(x)==len(attributes[0]), attributes[1:])) and len(attributes[0])==len(decisions))
    entropies, uniques = zip(*list(map(lambda x: calcEntropy(decisions, x), attributes)))
    #Decide our pivot attribute
    pivotIndex = entropies.index(min(entropies))
    branches = []
    newAttributes = []
    for i in uniques:







