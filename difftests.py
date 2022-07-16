def difftest(data):
    dist = {}
    b26 = False
    if max(data) > 10:
        b26 = True
    for i in range(len(data)-1):
        if b26 == True:
            diff = (data[i+1] - data[i]) % 26
        else:
            diff = (data[i+1] - data[i]) % 10
        dist[diff] = dist.get(diff,0) + 1
    return dist

def slopetest(data):
    dist = {}
    b26 = False
    if max(data) > 10:
        b26 = True
    for i in range(len(data)-2):
        if b26 == True:
            slopediff = (data[i+2] - 2*data[i+1] + data[i]) % 26
        else:
            slopediff = (data[i+2] - 2*data[i+1] + data[i]) % 10
        dist[slopediff] = dist.get(slopediff,0) + 1
    return dist

def max_diff_error(data):
    dist = difftest(data)
    maximum = max(dist,key=dist.get)
    expected = (len(data)-1)/len(dist)
    error = 100*(dist[maximum]-expected)/expected
    return (maximum,error)

def min_diff_error(data):
    dist = difftest(data)
    minimum = min(dist,key=dist.get)
    expected = (len(data)-1)/len(dist)
    error = 100*(dist[minimum]-expected)/expected
    return (minimum,error)

def max_slope_error(data):
    dist = slopetest(data)
    maximum = max(dist,key=dist.get)
    expected = (len(data)-2)/len(dist)
    error = 100*(dist[maximum]-expected)/expected
    return (maximum,error)

def min_slope_error(data):
    dist = slopetest(data)
    minimum = min(dist,key=dist.get)
    expected = (len(data)-2)/len(dist)
    error = 100*(dist[minimum]-expected)/expected
    return (minimum,error)

if __name__ == "__main__":
    data = [0,1,2,3,4,5,6,7,8,9,10]
    print(slopetest(data))
    print(max_slope_error(data))