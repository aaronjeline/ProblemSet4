from math import log
def calcEntropy(positives, negatives):
    if positives==0 or negatives==0:
        return 0
    q = positives/(positives+negatives)
    return -q * log(q,2) - (1-q) * log(1-q,2)

def rateAttribute(attribute, results):
    #Create a list of all the unique values of the attribute
    uniques,vals = [], []
    for i in attribute:
        if i not in uniques:
            uniques.append(i)
    for i in uniques:
        positives, negatives = 0,0
        for j in range(len(attribute)-1):
            if attribute[j]==i:
                if results[j]:
                    positives += 1
                else:
                    negatives += 1
        vals.append((positives, negatives))
    sums = map(lambda x: sum(x), vals)
    entropies = map(lambda x: calcEntropy(x[0],x[1]), vals)
    weightedAverage = None
    return weightedAverage





#decisions is a list of booleans, attributes is a list of lists containing attributes
def classify(decisions, attributes):
    #Check to make sure all the sizing works out
    assert(all(map(lambda x:len(x)==len(attributes[0]), attributes[1:])) and len(attributes[0])==len(decisions))
    ratings= map(lambda x:rateAttribute(x, decisions), attributes)

