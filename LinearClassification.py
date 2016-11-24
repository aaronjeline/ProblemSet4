from random import random

def hardThresholdStep(weights, stepSize, trainingVector, h, i):
    return weights[i] + stepSize(trainingVector[-1] - h(trainingVector[:-1], weights))trainingVector[i]

def h(weights, xVector):
    val = weights[1]*xVector[0] + weights[0]-xVector[1]
    if val >= 0:
        return 1
    else:
        return 0

def classify(trainingData, trainingFunction, stabilizationThreshold):
    attempts = []
    weights = tuple()
    #Generate our random weights
    stabilizationTime = 0
    while(stabilizationTime < stabilizationThreshold):

