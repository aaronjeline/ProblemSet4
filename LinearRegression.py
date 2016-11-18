def linearRegression(data):
    sampleSize = len(data)
    w1n = sampleSize * sum(data, key=lambda x:x[0]*x[1]) - sum(data, key=lambda x:x[0]) * sum(data, key=lambda x:x[1])
    w1d = sampleSize * sum(data, key=lambda x:x[0]**2) - sum(data, key=lambda x:x)**2
    w1 = w1n/w1d
    w0 = (sum(data, key=lambda x:x[1]) - w1 * sum(data, key= lambda x:x[0]))/sampleSize
    return w1,w0

