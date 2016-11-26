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
    return (random.randint(weightRange[0],weightRange[1]), random.randint(weightRange[0],weightRange[1]))

#Allows you to specify alternate starting weights
def classify(trainingData, trainingFunction, stabilizationThreshold, startingWeights=None):
    weights = tuple()
    if startingWeights == None:
        #Generate our random weights
        x0 = list(map(lambda x: x[0], trainingData))
        weightRange = (min(x0), max(x0))
        del x0
        weights = randomWeights(weightRange)
    stabilizationTime = 0
    stepSize = 0.1
    currentSolution = None
    while(stabilizationTime < stabilizationThreshold):
        newWeights = list(weights)
        sample = trainingData[random.randrange(len(trainingData))]
        for i in range(len(sample[:-1])):
            newWeights[i] = trainingFunction(weights, stepSize, sample, h, i)
        stabilizationTime += 1
        currentSolution = newWeights
    return currentSolution

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

solution = classify(trainingData, hardThresholdStep, 100000)

def drawPoint(data):
    c = ""
    if data[-1]==1:
        c = "red"
    else:
        c = "blue"
    return point((data[0],data[1]),color=c)

points = sum(map(drawPoint, trainingData))
final = plot(solution[0] * x + solution[1], 0, 10, color="green") + points
show(final)
