from logging import raiseExceptions
import math


def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs((x[i] - y[i]))
    return res

def jaccard_dist(x, y):
    intersection = 0
    union = 0
    if len(x) == 0 and len(y) == 0:
        return 1
    # elif len(x) == 0 or len(y) == 0:
    #     return 0

    for i in range(len(x)):
        if x[i] == y[i]:
            intersection += 1
        else:
            union += 1

    union += intersection
    return 1 - intersection/union        

def cosine_sim(x, y):
    if len(x) == 0 or len(y) == 0:
        return 1
    elif len(x) != len(y):
        return 0
    else:
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(x)):
            sumxx += x[i]*x[i]
            sumyy += y[i]*y[i]
            sumxy += x[i]*y[i]
        return sumxy/math.sqrt(sumxx*sumyy)
        # return manhattan_dist(x, y) / euclidean_dist(x, y)

# Feel free to add more
x = [0]
y = [0, 0]
print(euclidean_dist(x, y))