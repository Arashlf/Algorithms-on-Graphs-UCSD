#Uses python3

import sys

def Dijkstra(adj, cost, s, t):
    dist = n * [int(1e12)]
    # prev = n * [-1]
    dist[s] = 0
    H = ({x : dist[x] for x in range(n)})
    while H:
        u = min(H, key=H.get)
        del H[u]
        for idx, i in enumerate(adj[u]):
            if dist[i] > dist[u] + cost[u][idx]:
                dist[i] = dist[u] + cost[u][idx]
                # prev[i] = u       Doesn't need
                H[i] = dist[i]
    return dist[t]

def distance(adj, cost, s, t):
    dist = Dijkstra(adj, cost, s, t)
    return -1 if (dist == int(1e12)) else dist

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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))