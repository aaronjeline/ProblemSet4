import random

def hardThresholdStep(weights, stepSize, trainingVector, h, i):
    return weights[i] + stepSize * (trainingVector[-1] - h(weights, trainingVector[:-1]))*trainingVector[i]

def h(weights, xVector):
    val = weights[0]*xVector[0] + weights[1]-xVector[1]
    if val >= 0:
        return 2
    else:
        return 0

def randomWeights(weightRange):
    weights = (random.randint(weightRange[0],weightRange[1]), random.randint(weightRange[0],weightRange[1]))

#Allows you to specify alternate starting weights
def classify(trainingData, trainingFunction, stabilizationThreshold, startingWeights=randomWeights):
    attempts = []
    weights = tuple()
    #Generate our random weights
    x0 = list(map(lambda x: x[0], trainingData))
    weightRange = (min(x0), max(x0))
    weights = startingWeights(weightRange)
    del x0
    stabilizationTime = 0
    stepSize = 0.1
    while(stabilizationTime < stabilizationThreshold):
        newWeights = list(weights)
        sample = trainingData[random.randrange(len(trainingData))]
        for i in range(len(sample[:-1])):
            newWeights[i] = trainingFunction(weights, stepSize, sample, h, i)
        stabilizationTime += 1
        attempts.append(tuple(newWeights))
    return attempts

trainingData = [
    [3,2,0],
    [10,1,0],
    [1,10,1],
    [5,30,1],
    [5,6,0],
    [6,7,0],
    [10,8,0],
    [1,4,0],
    [1,20,1],
    [2,20,1],
    [3,20,1],
]
lines = classify(trainingData, hardThresholdStep, 10)
print(lines)
print(lines[1])
