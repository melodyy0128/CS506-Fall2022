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
    return manhattan_dist(x, y) / euclidean_dist(x, y)

def cosine_sim(x, y):
    return manhattan_dist(x, y) / euclidean_dist(x, y)

# Feel free to add more
