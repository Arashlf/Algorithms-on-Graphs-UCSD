#Uses python3
import sys

def prim(adj):
    cost = n * [1e5]
    # parent = n * [-1]
    cost[0] = 0
    PrioQ = ({v : cost[v] for v in range(n)})
    while PrioQ:
        v = min(PrioQ, key=PrioQ.get)
        del PrioQ[v]
        for idx, z in enumerate(adj[v]):
            if cost[idx] > z and idx in PrioQ:
                cost[idx] = z
                # parent[idx] = v
                PrioQ[idx] = cost[idx]
    return cost

def minimum_distance(x, y):
    result = 0.
    V = [v for v in range(n)]
    adj = [[((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5 for i in range(n)] for j in range(n)]
    result = prim(adj)
    return sum(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
