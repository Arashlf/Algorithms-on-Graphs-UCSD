#Uses python3

import sys

def distance_f(adj, dist2, s):
    dist = dist2.copy()
    queue = []
    queue.append(s)
    while queue:
        u = queue.pop(0)
        for idx, i in enumerate(adj[u]):
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[u] + 1
    return dist

def relax(dist, prev, u, v, cost):
    if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            prev[v] = u

def bellmanFord(adj, dist, prev, cost):
    for idx in range(n-1):
        for u, vs in enumerate(adj):
            for l, v in enumerate(vs):
                relax(dist, prev, u, v, cost[u][l])


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    dist = n * [int(1e7)]
    prev = n * [-1]
    dist[0] = 0
    bellmanFord(adj, dist, prev, cost)
    dist2 = dist.copy()
    A = set()
    for u, vs in enumerate(adj):
            for l, v in enumerate(vs):
                relax(dist2, prev, u, v, cost[u][l])
    shortest = distance_f(adj, dist2, s)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [0] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if shortest[x] != 0:
            print('-')
        elif reachable[x] == 0:
            print('*')
        else:
            print(distance[x])

