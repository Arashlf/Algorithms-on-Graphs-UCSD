#Uses python3

import sys

sys.setrecursionlimit(200000)

def cal_reverse(graph):
    gr = [[] for _ in graph]
    for i, l in enumerate(graph):
        for x in l:
            gr[x].append(i)
    return gr

def dfs(adj, visited, order, node):
    if not visited[node]:
        visited[node] = 1
        for neighbour in adj[node]:
            dfs(adj, visited, order, neighbour)
        order.append(node)


def number_of_strongly_connected_components(adj):
    visited = [0] * n
    order = []
    # DFS and finding post numbers
    for idx, i in enumerate(visited):
        if visited[idx] == 0:
            dfs(cal_reverse(adj), visited, order, idx)
    order.reverse()
    # SCCs
    result = 0
    visited2 = [0] * n
    temp = []
    for idx, i in enumerate(order):
        if visited2[i] == 0:
            result += 1
            dfs(adj, visited2, temp, i)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
