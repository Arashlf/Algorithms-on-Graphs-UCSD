#Uses python3

import sys

def dfs(adj, visited, order, node):
    if not visited[node]:
        visited[node] = 1
        for neighbour in adj[node]:
            dfs(adj, visited, order, neighbour)
        order.append(node)


def toposort(adj):
    visited = [0] * n
    order = []
    for idx, i in enumerate(visited):
        if visited[idx] == 0:
            dfs(adj, visited, order, idx)
    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

