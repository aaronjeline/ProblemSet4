from math import log
def calcEntropy(positives, negatives):
    if positives==0 or negatives==0:
        return 0
    q = positives/(positives+negatives)
    return -q * log(q,2) - (1-q) * log(1-q,2)

def rankAttribute(decisions, attribute):
    uniques, results = [], []
    for val in attribute:
        if val not in uniques:
            uniques.append(val)
    for val in uniques:
        positives, negatives = 0, 0
        for i in range(len(attribute)):
            if val == attribute[i]:
                if decisions[i]:
                    positives += 1
                else:
                    negatives += 1
        localSum = positives + negatives
        entropy = calcEntropy(positives, negatives)
        results.append((localSum, entropy))
    totalSum = sum(map(lambda x: x[1], results))
    weightedAverage = sum(map(lambda x: x[0]*x[1], results))/totalSum
    return (weightedAverage, uniques)



#decisions is a list of booleans, attributes is a list of lists containing attributes
def classify(decisions, attributes):
    #Check to make sure all the sizing works out
    assert(all(map(lambda x:len(x)==len(attributes[0]), attributes[1:])) and len(attributes[0])==len(decisions))
    entropies, uniques = zip(*list(map(lambda x: rankAttribute(decisions, x), attributes)))
    if all(map(lambda x:x==0,entropies)):
        #We have the simplist case, so return
        return "Done"
    #Decide our pivot attribute
    pivotIndex = entropies.index(min(entropies))
    pivotAttribute = attributes[pivotIndex]
    branches = []
    localAttributes = list(attributes)
    localAttributes.pop(pivotIndex)
    for i in uniques:
        newAttributes = []
        uniqueIndices = filter(lambda x: pivotAttribute[x]==i, range(len(pivotAttribute-1)))
        for j in localAttributes:
            newAttributes.append(list(map(lambda x:j[x], uniqueIndices)))
        #Recurse, and classify the simplified list
        branches.append(classify(decisions, newAttributes))
    return branches


A1 = [1,1,0,1,1]
A2 = [0,0,1,1,1]
A3 = [0,1,0,1,0]
Y = [False,False,False,True,True]
LA = [A1,A2,A3]
entropies = map(lambda x: rankAttribute(Y, x), LA)
print(list(entropies))
