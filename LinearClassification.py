import random

def hardThresholdStep(weights, stepSize, trainingVector, h, i):
    return weights[i] + stepSize * (trainingVector[-1] - h(weights, trainingVector[:-1])) * trainingVector[i]

def h(weights, xVector):
    val = weights[0]*xVector[0]+weights[1]*xVector[1]+weights[2]*xVector[2]
    if val >= 0:
        return 1
    else:
        return 0

def randomWeights(weightRange):
    return random.randint(weightRange[0],weightRange[1])


# Allows you to specify alternate starting weights
def classify(trainingData, trainingFunction):
    time = 0
    #Generate our random weights
    x0 = list(map(lambda x: x[0], trainingData))
    weightRange = (min(x0), max(x0))
    del x0
    weights = (randomWeights(weightRange), randomWeights(weightRange), randomWeights(weightRange))
    print("Starting Weights: ")
    print(weights)
    stepSize = 0.1
    currentSolution = None
    while time < 100000:
        stepSize = 1/10
        newWeights = list(weights)
        sample = trainingData[random.randrange(len(trainingData))]
        for i in range(len(sample[:-1])):
            newWeights[i] = trainingFunction(weights, stepSize, sample, h, i)
        time += 1
        currentSolution = newWeights
        weights = newWeights
    return currentSolution

trainingData = [
    [1,3,2,0],
    [1,10,1,0],
    [1,1,10,1],
    [1,5,30,1],
    [1,5,6,0],
    [1,6,7,0],
    [1,10,8,0],
    [1,1,4,0],
    [1,1,20,1],
    [1,2,20,1],
    [1,3,20,1],
]

solution = classify(trainingData, hardThresholdStep)

def drawPoint(data):
    c = ""
    if data[-1]==1:
        c = "red"
    else:
        c = "blue"
    return point((data[1],data[2]),color=c)

points = sum(map(drawPoint, trainingData))
final = plot(-(solution[1]/solution[2])*x-(solution[0]/solution[1])  , -1, 10, color="green") + points
show(final)
