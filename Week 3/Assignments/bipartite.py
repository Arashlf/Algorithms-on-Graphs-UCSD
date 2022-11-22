#Uses python3

import collections
import sys

def bipartite(adj):
    queue = collections.deque([])
    dist = n * [-1]
    for v in range(n):
        if dist[v] != -1:
            continue
        dist[v] = 0
        queue.append(v)
        while queue:
            u = queue.popleft()
            for i in adj[u]:
                if dist[i] == -1:
                    queue.append(i)
                    dist[i] = 1 - dist[u]
                elif dist[i] == dist[u]:
                    return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))