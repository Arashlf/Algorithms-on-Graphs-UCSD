#Uses python3

import sys

def relax(dist, prev, u, v, cost):
    if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            prev[v] = u

def bellmanFord(adj, dist, prev, cost):
    for idx in range(n-1):
        for u, vs in enumerate(adj):
            for l, v in enumerate(vs):
                relax(dist, prev, u, v, cost[u][l])

def negative_cycle(adj, cost):
    dist = n * [int(1e7)]
    prev = n * [-1]
    dist[0] = 0
    bellmanFord(adj, dist, prev, cost)
    dist2 = dist.copy()
    for u, vs in enumerate(adj):
            for l, v in enumerate(vs):
                relax(dist2, prev, u, v, cost[u][l])
    if dist == dist2:
        return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
