#Takes data, a list of tuples, each tuple containing: (x,y)
def linearRegression(data):
    sampleSize = len(data)
    w1n = sampleSize * sum(map(lambda x:x[0]*x[1], data)) - sum(map(lambda x:x[0], data)) * sum(map(lambda x:x[1], data))
    w1d = sampleSize * sum(map(lambda x:x[0]**2, data)) - sum(map(lambda x:x[0], data))**2
    w1 = w1n/w1d
    w0 = (sum(map(lambda x:x[1], data)) - w1 * sum(map(lambda x:x[0], data)))/sampleSize
    return w1,w0

simpleLine = [(2,3),(3,4),(4,5),(5,7)]
m, b = linearRegression(simpleLine)
graph = sum(map(lambda x:point((x[0],x[1]), color="red"), simpleLine))
graph += plot(m*x+b, 0, 6)
show(graph)