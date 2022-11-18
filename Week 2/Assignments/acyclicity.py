#Uses python3

import sys

def explore(adj, visited, v):
    visited[v] = -1
    for i in adj[v]:
        if visited[i] == 0:
            if explore(adj, visited, i):
                return 1
        elif visited[i] == -1:
            return 1
    visited[v] = 1

def acyclic(adj):
    visited = n * [0]
    for idx, i in enumerate(visited):
        if visited[idx] == 0:
            if explore(adj, visited, idx):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))